# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender", default="male")
    age = fields.Integer(string="Age")
    partner_role = fields.Selection([
        ('member', 'Member'),
        ('trainer', 'Trainer'),
    ], string="Partner Role", default="member")
    support_trainer = fields.Many2one('res.partner', string="Support Trainer", ondelete="cascade", domain=[('partner_role', '=', 'trainer')])
    trainer_skills = fields.Many2many('gym.trainer.skills', string="Skills", ondelete="cascade")