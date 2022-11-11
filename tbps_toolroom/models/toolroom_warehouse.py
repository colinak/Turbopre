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

class TrStockWarehouse(models.Model):
    _inherit = 'stock.warehouse'
    # _name = 'tr.stock.warehouse'
    # _description = 'Toolroom Warehouse'
    # _order = 'name'
    # _rec_name = 'name'

    # warehouse_id = fields.Many2one(
        # 'tr.stock.warehouse',
        # string="Almacén"
    # )
    # note = fields.Text(
        # string="Notas",
        # help="Notas para fines internos"
    # )
    # route_ids = fields.Many2many(
        # 'stock.location.route',
        # 'tr_stock_route_warehouse_rel',
        # 'warehouse_id',
        # 'route_id',
        # string="Rutas"
    # )
    # resupply_wh_ids= fields.Many2many(
        # 'tr.stock.warehouse',
        # 'tr_stock_wh_resupply_table_rel',
        # 'supplied_wh_id',
        # 'supplier_wh_id',
        # string="Resupply From"
    # )
    # pick_type_id = fields.Many2one('tr.stock.picking.type', 'Pick Type', check_company=True)
    # pack_type_id = fields.Many2one('tr.stock.picking.type', 'Pack Type', check_company=True)
    # out_type_id = fields.Many2one('tr.stock.picking.type', 'Out Type', check_company=True)
    # in_type_id = fields.Many2one('tr.stock.picking.type', 'In Type', check_company=True)
    # int_type_id = fields.Many2one('tr.stock.picking.type', 'Internal Type', check_company=True)

