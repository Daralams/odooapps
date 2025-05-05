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
    is_member = fields.Boolean(string="Is Gym Member", default=False)
    member_id = fields.Char(string="Member ID", default=lambda self: _('New'), readonly=True, copy=False, help="Unique member ID for each registered member")
    support_trainer = fields.Many2one('hr.employee', string="Support Trainer", ondelete="cascade", domain=[('is_trainer', '=', True), ('active', '=', True)])
    join_date = fields.Date(string="Join Date", default=fields.Date.today(), required=True)
    exit_date = fields.Date(string="Exit Date", default=fields.Date.today(), required=True)
    status = fields.Selection([
        ('waiting', 'Waiting'),
        ('joined', 'Joined'),
        ('exit', 'Exit'),
        ('expired', 'Expired'),
    ], default="waiting", copy=False)
    member_detail_ids = fields.One2many(comodel_name="gym.membership.detail", inverse_name="membership_id")    
    workouts_plan_ids = fields.One2many(comodel_name="gym.workouts.plan", inverse_name="partner_id", string="Workout Plan")
    diet_plan_ids = fields.One2many(comodel_name="gym.diet.plan", inverse_name="partner_id", string="Diet Plan")

    def action_joined(self):
        self.status = 'joined'

    def action_exit(self):
        self.status = 'exit'

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
        
        if vals.get('is_member') == True and vals.get('member_id', _('New')) == _('New'):
            vals['member_id'] = self.env['ir.sequence'].next_by_code('res.partner.member')
        return super(Partner, self).create(vals)

    def write(self, vals):
        """Automatically generate a Member ID and Trainer ID number for gym management."""
        
        if vals.get('is_member') == True and self.member_id == _('New'):
            vals['member_id'] = self.env['ir.sequence'].next_by_code('res.partner.member')
        return super(Partner, self).write(vals)