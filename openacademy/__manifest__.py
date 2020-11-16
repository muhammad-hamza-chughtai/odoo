# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Manage Trainings """,
    'sequence': '-8',

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        
        'views/partner.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'wizards/wizard_view.xml',
        'reports/report.xml',
        'reports/session_board.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [],
    'installabe': True,
    'application': True,
    'autoinstall': False,
}
