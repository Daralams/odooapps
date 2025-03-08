from odoo import models, fields, api

class GymWorkoutsPlan(models.Model):
    _name = 'gym.workouts.plan'
    _description = 'Gym Workouts Plan'

    workout_id = fields.Many2one('gym.workouts', string="Name", ondelete="cascade")
    partner_id = fields.Many2one('res.partner', string="Member", domain=[('partner_role', '=', 'member'), ('status', '=', True)], ondelete="cascade")
    start_date = fields.Date(string="From", required=True)
    end_date = fields.Date(string="To", required=True)