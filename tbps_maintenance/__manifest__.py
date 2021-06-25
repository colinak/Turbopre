#!/usr/bin/env python3
# -*- coding: utf-8 -*-

{
    'name': "Tbps Maintenance",
    'version': "14.0.1",
    'author': "Kewitz Colina",
    'website': "https://github.com/colinak",
    'summary': "Maintenance Turbopre",
    'sequence': 10,
    'description': "Maintenance Turbopre",
    'category': "mail",
    'depends': [
        'base',
        'maintenance',
        'hr',
        'hr_maintenance'
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/equipment_assignment_report.xml',
        'wizards/replace_equipment_wizard.xml',
        'views/maintenance_equipment_category_view.xml',
        'views/maintenance_manufacturers_view.xml',
        'views/maintenance_equipment_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}


