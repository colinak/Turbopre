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
    'depends': [
        'base',
        'hr',
    ],
    'data': [
        "data/data_status.xml",
        "data/quality.activity.type.csv",
        "data/quality.equipment.category.csv",
        "data/quality.equipment.clasification.csv",
        "data/quality.equipment.manufacturers.csv",
        "security/quality_security.xml",
        "security/quality_traceability_equipment/ir.model.access.csv",
        "security/quality_equipment_manufacturers/ir.model.access.csv",
        "security/quality_equipment_clasification/ir.model.access.csv",
        "security/quality_equipment_category/ir.model.access.csv",
        "security/quality_activity_type/ir.model.access.csv",
        "security/quality_status/ir.model.access.csv",
        "security/quality_equipment/ir.model.access.csv",
        "security/quality_location/ir.model.access.csv",
        "security/quality_loans_returns/ir.model.access.csv",
        "security/quality_employee/ir.model.access.csv",
        "views/menu_setting_view.xml",
        "views/quality_equipment_manufacturers_view.xml",
        "views/quality_equipment_clasification_view.xml",
        "views/quality_equipment_category_view.xml",
        "views/quality_activity_type_view.xml",
        "views/quality_status_view.xml",
        "views/quality_location_view.xml",
        "views/quality_equipment_view.xml",
        "views/quality_loans_returns_view.xml",
        "views/quality_tps_employee_view.xml",
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
