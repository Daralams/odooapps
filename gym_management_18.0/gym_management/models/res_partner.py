# -*- coding: utf-8 -*-

from odoo import models, fields, Command, api, _
from odoo.exceptions import ValidationError

class Partner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender", default="male")
    age = fields.Integer(string="Age")
    partner_role = fields.Selection([
        ('member', 'Member'),
        ('trainer', 'Trainer'),
    ], string="Partner Role", default="member")
    member_id = fields.Char(string="Member ID", default=lambda self: _('New'), readonly=True, copy=False, help="Unique member ID for each registered member")
    trainer_id = fields.Char(string="Trainer ID", default=lambda self: _('New'), readonly=True, copy=False, help="Unique trainer ID for each registered trainer")
    support_trainer = fields.Many2one('res.partner', string="Support Trainer", ondelete="cascade", domain=[('partner_role', '=', 'trainer'), ('status', '=', 'joined')])
    trainer_skills = fields.Many2many('gym.trainer.skills', string="Skills", ondelete="cascade")
    join_date = fields.Date(string="Join Date", default=fields.Date.today(), required=True)
    left_date = fields.Date(string="Left Date", default=fields.Date.today(), required=True)
    status = fields.Selection([
        ('waiting', 'Waiting'),
        ('joined', 'Joined'),
        ('left', 'Left'),
        ('expired', 'Expired'),
    ], default="waiting", copy=False)
    member_detail_ids = fields.One2many(comodel_name="gym.membership.detail", inverse_name="membership_id")    
    workouts_plan_ids = fields.One2many(comodel_name="gym.workouts.plan", inverse_name="partner_id", string="Workout Plan")

    def action_joined(self):
        self.status = 'joined'

    def action_left(self):
        self.status = 'left'

    def action_to_waiting(self):
        self.status = 'waiting'


    def action_create_invoice(self):
            for record in self:
                if record.member_detail_ids:
                    for membership in record.member_detail_ids:
                        invoice = membership.env["account.move"].create(
                            {
                                "partner_id": membership.membership_id.id,
                                "move_type": "out_invoice",
                                "invoice_line_ids": [
                                    Command.create({
                                        "name": membership.membership_type.name,
                                        "quantity": membership.membership_time,
                                        "price_unit": membership.membership_type.fees
                                    })
                                ]
                            }
                        )
                        membership.invoice_number = invoice.name
                        # return action untuk redirect ke form invoice yang baru dibuat
                        return {
                            'name': _('Customer Invoice'),
                            'view_mode': 'form',
                            'res_model': 'account.move',
                            'res_id': invoice.id,
                            'type': 'ir.actions.act_window',
                            'context': {'create': False},
                        }
                else:
                    raise ValidationError("Cannot create invoice if membership details are empty.")

    @api.model
    def create(self, vals):
        """Automatically generate a Member ID and Trainer ID number for gym management."""
        
        if vals.get('partner_role') == 'member' and vals.get('member_id', _('New')) == _('New'):
            vals['member_id'] = self.env['ir.sequence'].next_by_code('res.partner.member')

        if vals.get('partner_role') == 'trainer' and vals.get('trainer_id', _('New')) == _('New'):
            vals['trainer_id'] = self.env['ir.sequence'].next_by_code('res.partner.trainer')
        return super(Partner, self).create(vals)