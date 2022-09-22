# -*- coding: utf-8 -*-


from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    target_sales_invoiced = fields.Integer('Invoiced in Sales Orders Target')
