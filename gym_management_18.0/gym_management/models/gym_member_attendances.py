from odoo import models, fields, api

class GymMemberAttendances(models.Model):
    _name = 'gym.member.attendances'
    _description = 'Gym Member Attendances'
    _order = 'id desc'

    name = fields.Many2one('res.partner', string="Name", domain=[('partner_role', '=', 'member'), ('status', '=', 'joined')])
    check_in = fields.Datetime(string="Check in", default=fields.Datetime.now(), required=True)
    check_out = fields.Datetime(string="Check out", required=True)
    time_spent = fields.Char(string="Time Spent", compute="_compute_total_time", default=0)
    feedback = fields.Text(string="Feedback")

    @api.depends('time_spent')
    def _compute_total_time(self):
        for record in self:
            time_spent_total = str(record.check_out - record.check_in)
            record.time_spent = time_spent_total
