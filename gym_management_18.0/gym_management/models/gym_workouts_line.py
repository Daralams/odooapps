from odoo import models, fields, api

class GymWorkoutsLine(models.Model):
    _name = 'gym.workouts.line'
    _description = 'Gym Workouts Line'

    workout_id = fields.Many2one('gym.workouts', ondelete='cascade')
    name = fields.Char(string='Exercise Name')
    calories_burn = fields.Integer(string="Calories Burn")
    exercise_for = fields.Many2many('gym.workouts.exercise', string="Exercise for", ondelete="cascade")
    equipments = fields.Many2one('product.template', string="Equipments", domain=[('gym_equipment_ok', '=', True)], ondelete="cascade")
    sets = fields.Integer(string="Sets")
    repeat = fields.Integer(string="Repeat")
    weight = fields.Float(string="Weight (kg)")
    average_time = fields.Float(string="Average Time (Minutes)")
    steps = fields.Html('Steps', translate=True)
    benefits = fields.Html('Benefits', translate=True)
    # field Gym line in inventory: weight, quantity, condition (fungsi, rusak), dsb