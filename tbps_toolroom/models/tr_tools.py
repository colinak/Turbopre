#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
#
# Author: KEWITZ COLINA
# Copyleft: 2020-Present.
# License LGPL-3.0 or later (http: //www.gnu.org/licenses/lgpl.html).
#
###############################################################################

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class ToolRoomTools(models.Model):
    _inherit = 'product.product'


    employee_id = fields.Many2one(
        "hr.employee",
        string="Empleado"
    )
    inventory_id = fields.Many2one(
        "tr.stock.inventory",
        string="Inventario"
    )
    available_qty = fields.Integer(
        "Cantidad disponible", 
        compute='_compute_available_qty', 
        # search='_search_qty_available',
        # compute_sudo=False,
    )
    lot_ids = fields.One2many(
        "tr.stock.production.lot",
        "product_id",
        string="Serial Producto"
    )
    product_serial_count = fields.Integer(
        string="Herramientas",
        compute="_compute_tools_count"
    )


    def _compute_available_qty(self):
        for rec in self:
            rec.available_qty = rec.lot_ids.search_count([
                ('state', '=', 'done'),
                ('product_id.id', '=', rec.id)
            ])


