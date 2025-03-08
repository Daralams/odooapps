from odoo import models, fields, api

class GymWorkoutsExercise(models.Model):
    _name = 'gym.workouts.exercise'
    _description = 'Gym Workouts Exercise'

    name = fields.Char(string="Name")
    color = fields.Integer(string="color")