from odoo import models, fields, api, _

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    is_trainer = fields.Boolean(string="Is Gym Trainer", default=False)
    trainer_id = fields.Char(string="Trainer ID", default=lambda self: _('New'), readonly=True, copy=False, help="Unique trainer ID for each registered trainer")
    active = fields.Boolean(string="Active", default=True, help="This record is active or inactive")

    @api.model
    def create(self, vals):
        if vals.get('is_trainer'):
            vals['trainer_id'] = self.env['ir.sequence'].next_by_code('hr.employee.trainer')
        return super(HrEmployee, self).create(vals)

    def write(self, vals):
        if vals.get('is_trainer') and self.trainer_id == _('New'):
            vals['trainer_id'] = self.env['ir.sequence'].next_by_code('hr.employee.trainer')
        return super(HrEmployee, self).write(vals)