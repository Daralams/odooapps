from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_post(self):
        res = super(AccountMove, self).action_post()
        for invoice in self:
            membership = self.env['gym.membership.detail'].search([('membership_id', '=', invoice.partner_id.id)], limit=1)
            if membership:
                membership.invoice_number = invoice.name
                membership.state = 'in progress'
        return res