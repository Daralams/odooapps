from odoo import models, fields, api

class GymWorkouts(models.Model):
    _name = 'gym.workouts'
    _description = 'Gym Workouts'

    name = fields.Char(string="Name", required=True)
    image = fields.Binary(string="Image")
    support_trainer = fields.Many2one('res.partner', string="Support Trainer", domain=[('partner_role', '=', 'trainer'), ('status', '=', 'joined')])
    user_id = fields.Many2one('res.partner', default=lambda self: self.env.user)
    workout_days = fields.Many2many('gym.workout.days', string="Workout Days")
    description = fields.Html(
        'Description', translate=True)
    active = fields.Boolean(default=True)
    workout_ids = fields.One2many(comodel_name='gym.workouts.line', inverse_name='workout_id', string="Workouts Line")