from odoo import models, fields, api

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    def action_create_payments(self):
        res = super(AccountPaymentRegister, self).action_create_payments()
        for invoice in self:
            membership = self.env['gym.membership.detail'].search([('membership_id', '=', invoice.partner_id.id)], limit=1)
            if membership:
                membership.state = 'done'
        return res