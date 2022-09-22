# -*- coding: utf-8 -*-


from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    invoice_policy = fields.Boolean(string="Invoice Policy", help="Timesheets taken when invoicing time spent")
