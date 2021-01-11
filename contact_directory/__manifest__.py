#!/usr/bin/env python3
# -*- coding: utf-8 -*-

{
    'name': "Contact Directory",
    'version': "1.0",
    'author': "Kewitz Colina",
    'website': "https://github.com/colinak",
    'summary': "Directorio de Contactos Turbopre",
    'sequence': 10,
    'description': "Directorio de Contactos Turbopre",
    'category': "Employee",
    'depends': ['base', 'hr'],
    'data': [
        'views/contact_directory_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}
