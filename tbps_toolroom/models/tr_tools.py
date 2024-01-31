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
    total_qty = fields.Integer(
        "Cantidad Total",
        compute='_compute_total_qty',
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
            rec.available_qty = rec.product_variant_ids.lot_ids.search_count([
                ('product_id', '=', rec.id),
                ('stage', '=', 'available')
            ])

    def _compute_total_qty(self):
        for rec in self:
            rec.total_qty = rec.product_variant_ids.lot_ids.search_count([
                ('product_id', '=', rec.id),
                ('state', '=', 'done')
            ])


    def action_open_total_quants(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("tbps_toolroom.action_tr_stock_quant")
        action['domain'] = [('product_id', 'in', self.ids)]
        return action


    def action_open_available_quants(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("tbps_toolroom.action_tr_stock_production_lot")
        action['domain'] = [
            ('product_id', 'in', self.ids), 
            ('state', '=', 'done'),
            ('stage', '=', 'available'),
        ]
        return action


    def action_view_tr_stock_move_lines(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("tbps_toolroom.tr_stock_move_line_action")
        action['domain'] = [('product_id', 'in', self.ids)]
        return action



