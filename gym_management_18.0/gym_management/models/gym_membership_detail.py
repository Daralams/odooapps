from odoo import models, fields, api, _

class GymMembershipDetail(models.Model):
    _name = 'gym.membership.detail'
    _order = 'id desc'

    name = fields.Char(string="Membership No", default=lambda self: _("New"), readonly=True, copy=False, help="Unique Sequence No for each membership")
    membership_id = fields.Many2one('res.partner', string="Member Name", ondelete="cascade", domain=[('partner_role', '=', 'member'), ('status', '=', 'joined')])
    membership_type = fields.Many2one('gym.membership.type', string="Membership", ondelete="cascade")
    membership_time = fields.Integer(string="Membership Time/Mounth")
    fees_total = fields.Float(string="Fees Total", compute="_compute_fees_total")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in progress', 'In Progress'),
        ('done', 'Done'),
    ], string="State", default="draft", copy=False)
    active = fields.Boolean(string="Active" ,default=True)
    invoice_number = fields.Char(string="Invoice", readonly=True, copy=False)

    @api.depends('fees_total')
    def _compute_fees_total(self):
        for record in self:
            if record.membership_type:
                record.fees_total = record.membership_type.fees * record.membership_time

    @api.model
    def create(self, vals):
        """Automatically generate a Membership Number."""
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('gym.membership.detail')
        return super(GymMembershipDetail, self).create(vals)

    def action_open_related_member_name(self):
        action = self.env['ir.actions.actions']._for_xml_id('gym_management.gym_member_action')
        view_id = self.env.ref('gym_management.res_partner_view_form_inherit').id
        action['res_id'] = self.membership_id.id
        action['views'] = [[view_id, 'form']]
        return action

    def check_membership_expired(self):
        """ Check date end date of membership """
        date_now = fields.Date.today()
        membership_expired = self.search([('state', '=', 'done'), ('end_date', '<', date_now)])
        if membership_expired:        
            for rec in membership_expired:
                rec.active = False