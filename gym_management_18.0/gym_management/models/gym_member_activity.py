from odoo import models, fields, api, _

class GymMemberActivity(models.Model):
    _name = 'gym.member.activity'
    _description = 'Gym Member Activity'
    _order = 'id desc'

    attendance_id = fields.Many2one('hr.attendance', string="Attendance", ondelete="cascade")   
    name = fields.Many2one('res.partner', string="Member", domain=[('is_member', '=', True), ('status', '=', 'joined')], ondelete="cascade")
    exercise = fields.Many2one('gym.workouts.line', string="Exercise", ondelete="cascade")
    equipment = fields.Many2one('product.template', string="Equipment", domain=[('gym_equipment_ok', '=', True)], ondelete="cascade") 
    sets = fields.Integer(string="Sets")
    repeat = fields.Integer(string="Repeat")
    weight = fields.Float(string="Weight (kg)")
    date = fields.Date(string="Date")