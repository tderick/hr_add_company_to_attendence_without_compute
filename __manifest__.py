# -*- coding: utf-8 -*-
{
    'name': "hr_add_company_to_attendence_without_compute",

    'summary': """Add the company address to every attendence records in a form of string""",

    'author': "DERICK TEMFACK",
    'website': "https://github.com/tderick/hr_add_company_to_attendence_without_compute",
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['hr_attendance'],
    'application': False,
    'installable': True,
    'licence': 'LGPL-3',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/attendance_view.xml',
    ]
}
