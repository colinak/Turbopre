#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': "Tbps Quiality Equipment",
    'author': "Kewitz Colina",
    'website': "https://github.com/colinak",
    'version': "14.0.1",
    'sequence': 100,
    'category': "Manufacturing/Quiality",
    'summary': "Registration and control of quality control equipment",
    'description': """
        Registration, monitoring and control of quality control equipment loans
    """,
    'depends': ['base'],
    'data': [
        "data/data_status.xml", 
        "security/quality_equipment_manufacturers/ir.model.access.csv", 
        "security/quality_equipment_clasification/ir.model.access.csv", 
        "security/quality_equipment_category/ir.model.access.csv", 
        "security/quality_status/ir.model.access.csv", 
        "security/quality_equipment/ir.model.access.csv", 
        "views/menu_setting_view.xml", 
        "views/quality_equipment_manufacturers_view.xml", 
        "views/quality_equipment_clasification_view.xml", 
        "views/quality_equipment_category_view.xml", 
        "views/quality_status_view.xml", 
        "views/quality_equipment_view.xml", 
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
