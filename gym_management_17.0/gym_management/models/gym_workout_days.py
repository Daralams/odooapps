from odoo import models, fields, api

class GymWorkoutDays(models.Model):
    _name = 'gym.workout.days'
    _description = 'Gym Workout Days'

    name = fields.Char(string="Name")
    color = fields.Integer(string="Color")