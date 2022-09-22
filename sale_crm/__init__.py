# -*- coding: utf-8 -*-


from . import models
from . import wizard

from odoo import api, SUPERUSER_ID

def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    teams = env['crm.team'].search([('use_opportunities', '=', False)])
    teams.write({'use_opportunities': True})