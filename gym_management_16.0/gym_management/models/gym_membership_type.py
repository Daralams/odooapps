from odoo import models, fields, api

class GymMembershipType(models.Model):
    _name = 'gym.membership.type'
    _description = 'Gym Membership type'

    name = fields.Char(string="Name", required=True)
    duration = fields.Integer(string="Duration (mounths)", required=True)
    fees = fields.Float(string="Fees", required=True)
    benefits = fields.Text(string="Benefits")
    active = fields.Boolean(string="Active", default=True)

