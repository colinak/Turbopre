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
        'hr_maintenance',
        'tbps_mail_templates',
        'tbps_header_footer_layout'
    ],
    'data': [
        "data/maintenance.activity.csv",
        "data/maintenance.location.csv",
        'security/ir.model.access.csv',
        'security/maintenance_security.xml',
        'report/equipment_assignment_report.xml',
        'report/equipment_unassigned_report.xml',
        'report/resport_assigment_equipments.xml',
        'views/equipment_request_view.xml',
        'views/maintenance_equipment_category_view.xml',
        'views/maintenance_manufacturers_view.xml',
        'views/maintenance_activity_view.xml',
        'views/maintenance_equipment_view.xml',
        'views/maintenance_location_view.xml',
        'wizards/equipment_assignment_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}
