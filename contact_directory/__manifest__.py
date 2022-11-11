#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Author: KEWITZ COLINA
# Copyleft: 2020-Present.
# License LGPL-3.0 or later (http: //www.gnu.org/licenses/lgpl.html).
#
#
###############################################################################


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
