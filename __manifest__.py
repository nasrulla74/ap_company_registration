{
    'name': 'Appeul Company Registration',
    'version': '1.0.0',
    'summary': 'Appeul Company Registration',
    'description': """Appeul Company Registration""",
    'author': 'Appeul Services',
    'company': 'Appeul',
    'maintainer': 'Appeul Services',
    'category': 'Sales',
    'website': 'https://www.appeul.com',
    'sequence':"-1110",
    'depends': ['ap_personal_info'],
    'data': [
        'security/ir.model.access.csv',
        # 'data/sequence.xml',
        'views/company_reg_view.xml',
        'views/menu.xml',
        'report/memorandum.xml',
        'report/article_association.xml',
        'report/md_declaration.xml',
        'report/secretary_declaration.xml',
        'report/tax_declaration.xml',
        'report/report.xml',

    ],

    'installable': True,
    'application': True,


    'license': 'LGPL-3',

}