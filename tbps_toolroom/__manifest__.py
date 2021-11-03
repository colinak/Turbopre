#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': "Tbps ToolRoom",
    'author': "Kewitz Colina",
    'website': "https://github.com/colinak",
    'version': "14.0.1",
    'sequence': 100,
    'category': "Manufacturing/Equipment",
    'summary': "Registration and control of tools and equipment in the toolroom",
    'description': """
        Registration, monitoring and control of tools and equipment.
    """,
    'depends': [
        'base',
        'uom'
    ],
    'data': [
        "security/tools_manufacturers/ir.model.access.csv",
        "security/tools_category/ir.model.access.csv",
        "security/tools_equipment/ir.model.access.csv",
        "views/menu_setting_view.xml",
        "views/toolroom_manufacturers_view.xml",
        "views/toolroom_category_view.xml",
        "views/toolroom_equipment_view.xml",
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
