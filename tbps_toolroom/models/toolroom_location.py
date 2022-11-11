#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Author: KEWITZ COLINA
# Copyleft: 2020-Present.
# License LGPL-3.0 or later (http: //www.gnu.org/licenses/lgpl.html).
#
#
###############################################################################


from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)


class TrStockLocation(models.Model):
    _inherit = "stock.location"
    # _parent_name = "location_id"
    # _parent_store = True
    # _order = 'complete_name'
    # _rec_name = 'complete_name'


    # location_id = fields.Many2one(
        # 'tr.stock.location',
        # string="Parent location",
        # domain="[('company_id', 'in', [company_id, False])]",
        # help="La ubicación Principal, que incluye esta ubicación"
    # )


# class ToolroonRoute(models.Model):
    # _name = 'tr.stock.location.route'
    # _inherit = 'stock.location.route'
    # _description = "Inventory Routes"


    # product_ids = fields.Many2many(
        # 'toolroom.equipment',
        # 'tr_stock_route_product_rel',
        # 'route_id',
        # 'equipment_id',
        # string="Equipos"
    # )
    # categ_ids = fields.Many2many(
        # 'toolroom.category',
        # 'tr_stock_location_route_category_rel',
        # 'route_id',
        # 'categ_id',
        # string=u"Categoría de Producto"
    # )
    # warehouse_ids = fields.Many2many(
        # 'tr.stock.location',
        # 'tr_stock_route_warehouse_rel',
        # 'route_id',
        # 'warehouse_id',
        # string="Alamacenes"
    # )
