from odoo import models, fields, api

class GymDietPlanLine(models.Model):
    _name = 'gym.diet.plan.line'
    _description = 'Gym diet plan line'

    diet_id = fields.Many2one('gym.diet.plan', string="Diet Plan", ondelete="cascade")
    name = fields.Char(string="Diet Food", required=True)
    quantity = fields.Integer(string="Quantity (gr)")
    consume_at = fields.Char(string="Consume at")
