from odoo import models, fields, api

class GymDietPlan(models.Model):
    _name = 'gym.diet.plan'
    _description = 'Gym Diet Plan'

    name = fields.Char(string="Name", required=True)
    diet_ids = fields.One2many(comodel_name="gym.diet.plan.line", inverse_name="diet_id", string="Diet List")
    date = fields.Date(string="Date")