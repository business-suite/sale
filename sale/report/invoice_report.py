# -*- coding: utf-8 -*-


from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    team_id = fields.Many2one('crm.team', string='Sales Team')

    def _select(self):
        return super(AccountInvoiceReport, self)._select() + ", move.team_id as team_id"
