from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    gym_equipment_ok = fields.Boolean(string="Gym Equipment", help="does it include gym equipment?")