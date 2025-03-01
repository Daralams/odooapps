from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class GymTrainerAttendances(models.Model):
    _name = 'gym.trainer.attendances'
    _description = 'Gym trainer attendances'

    name = fields.Many2one('res.partner', string="Trainer", domain=[('partner_role', '=', 'trainer')], required=True)
    working_hours = fields.Float(string="Working Hours/Day")
    check_in = fields.Datetime(string="Check In", default=fields.Datetime.now(), required=True)
    check_out = fields.Datetime(string="Check Out", required=True)
    time_spent = fields.Char(string="Time Spent", compute="_compute_total_time", default=0)
    attendance_status = fields.Selection([
        ('finished', 'Finished'),
        ('unfinished', 'Unfinished'),
    ], string="Attendance Status", compute="_compute_attendance_status")

    @api.constrains('check_out')
    def _check_out_value(self):
        for record in self:
            if record.check_out < record.check_in:
                raise ValidationError('The check out cannot be set in the past.')
            
    
    @api.depends('time_spent')
    def _compute_total_time(self):
        for record in self:
            time_spent_total = str(record.check_out - record.check_in)
            record.time_spent = time_spent_total
    
    @api.depends('attendance_status')
    def _compute_attendance_status(self):
        for record in self:
            if record.time_spent:
                # ubah 'HH:MM:SS' ke total jam desimal
                time_parts = datetime.strptime(record.time_spent, "%H:%M:%S")
                time_spent = time_parts.hour + time_parts.minute / 60 + time_parts.second / 3600
            else:
                time_spent = 0  # jika tidak ada nilai, anggap 0 jam

            if record.working_hours > time_spent:
                record.attendance_status = 'unfinished'
            else:
                record.attendance_status = 'finished'
