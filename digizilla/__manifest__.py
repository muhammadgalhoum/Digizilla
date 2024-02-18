# -*- coding: utf-8 -*-
{
    'name': "Digizilla Custom Module",
    'summary': """Digizilla Custom Module""",
    'description': """""",
    'author': "Muhammad Galhoum",
    'website': "https://muhammadgalhoum.me",
    'category': 'uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/digizilla_views.xml',
        'views/tag_views.xml',
        'report/digizilla_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'digizilla/static/src/js/hiding_create_btn.js',
        ],
    },

    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}