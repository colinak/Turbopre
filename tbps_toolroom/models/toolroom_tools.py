#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class ToolRoomTools(models.Model):
    _inherit = 'product.product'
    _name = 'toolroom.tools'
    _description = 'Toolroom Tools'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Name",
    )
    category_id = fields.Many2one(
        'toolroom.category',
        string="Product Category",
        required=True,
        help="Seleccionar categoría para el producto actual"
    )
    route_ids = fields.Many2many(
        'stock.location.route',
        'tr_stock_route_tools_rel',
        'tool_id',
        'route_id',
        string="Rutas"
    )


