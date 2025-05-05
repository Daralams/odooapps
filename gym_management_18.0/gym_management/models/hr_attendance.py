from odoo import models, fields, api

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'
    
    member_activity_ids = fields.One2many(comodel_name='gym.member.activity', inverse_name='attendance_id', string="Member Activity", required=True)