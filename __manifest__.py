{
    'name': 'Digizilla',
    'version': '19.0.1.0.0',
    'category': 'Custom',
    'summary': '',
    'description': '',
    'author': 'Digizilla',
    'depends': ['base', 'sale_management', 'mail'],
    'data': [
        'security/digizilla_security.xml',
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'views/digizilla_menu.xml',
        'report/digizilla_report.xml',
        'report/digizilla_report_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'digizilla/static/src/js/digizilla_form.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
