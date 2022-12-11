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
        'product',
        'uom',
        'hr'
    ],
    'data': [
        "data/product.category.csv",
        "data/tr.stock.location.csv",
        "security/tr_warehouse/ir.model.access.csv",
        "security/tr_location/ir.model.access.csv",
        "security/tr_stock_picking/ir.model.access.csv",
        "security/tools_category/ir.model.access.csv",
        "security/tr_stock_inventory/ir.model.access.csv",
        "security/tr_stock_quant/ir.model.access.csv",
        "security/tr_stock_production_lot/ir.model.access.csv",
        # "security/tr_check_availability/ir.model.access.csv",
        "views/menu_setting_view.xml",
        "views/tr_warehouse_view.xml",
        "views/tr_stock_location_view.xml",
        "views/tr_product_category_view.xml",
        "views/tr_stock_picking_view.xml",
        "views/tr_stock_quant_view.xml",
        "views/tr_product_attribute_view.xml",
        "views/toolroom_equipment_view.xml",
        "views/toolroom_product_view.xml",
        "views/tr_stock_production_lot_view.xml",
        "views/hr_employee_view.xml",
        "views/tr_stock_inventory_view.xml",
        # "wizards/check_availability_tools_wizard.xml",
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
