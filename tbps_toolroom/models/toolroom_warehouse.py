#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class TrStockWarehouse(models.Model):
    _inherit = 'stock.warehouse'
    _name = 'tr.stock.warehouse'
    _description = 'Toolroom Warehouse'
    _order = 'name'
    _rec_name = 'name'


    note = fields.Text(
        string="Notas",
        help="Notas para fines internos"
    )
    route_ids = fields.Many2many(
        'stock.location.route',
        'tr_stock_route_warehouse_rel',
        'warehouse_id',
        'route_id',
        string="Rutas"
    )
    resupply_wh_ids= fields.Many2many(
        'tr.stock.warehouse',
        'tr_stock_wh_resupply_table_rel',
        'supplied_wh_id',
        'supplier_wh_id',
        string="Resupply From"
    )
