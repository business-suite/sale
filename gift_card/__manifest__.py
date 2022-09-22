# -*- coding: utf-8 -*-


{
    'name': "Gift Card",
    'summary': "Use gift card",
    'description': """Integrate gift card mechanism""",
    'category': 'Sales/Sales',
    'version': '1.0',
    'depends': ['product'],
    'data': [
        'data/gift_card_data.xml',
        'views/views.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'LGPL-3',
}
