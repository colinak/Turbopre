#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class ToolRoomEquipment(models.Model):
    _inherit = 'product.template'
    _name = 'toolroom.equipment'
    _description = 'Toolroom Equipment'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Name",
    )
    # type = fields.Selection(
        # default='product',
        # readonly=True,
    # )
    category_id = fields.Many2one(
        'toolroom.category',
        string="Product Category",
        required=True,
        help="Seleccionar categoría para el producto actual"
    )
    route_ids = fields.Many2many(
        'stock.location.route',
        'tr_stock_route_equipment_rel',
        'equipment_id',
        'route_id',
        string="Rutas"
    )


    # identification_code = fields.Char(string="Identification Code")
    # location = fields.Char(string="Location")
    # serial_number = fields.Char(string="Serial Number")

