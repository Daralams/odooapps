from odoo import models, fields, api

class GymTrainerSkills(models.Model):
    _name = 'gym.trainer.skills'
    _description = 'Gym Trainer Skills'

    name = fields.Char(string="Name")
    color = fields.Integer(string="Color")