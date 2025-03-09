from odoo import models, fields, api

class GymDietPlan(models.Model):
    _name = 'gym.diet.plan'
    _description = 'Gym Diet Plan'

    name = fields.Char(string="Name", required=True)
    partner_id = fields.Many2one("res.partner", string="Member", ondelete="cascade")
    diet_ids = fields.One2many(comodel_name="gym.diet.plan.line", inverse_name="diet_id", string="Diet List")
    date = fields.Date(string="Date")