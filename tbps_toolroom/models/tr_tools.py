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
from odoo.exceptions import UserError
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
        compute="_compute_available_qty",
        search='_search_qty_available',
    )
    total_qty = fields.Integer(
        "Cantidad Total",
        compute='_compute_total_qty',
        search='_search_total_qty',
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
    availability = fields.Boolean(
        "Disponible?",
        default=lambda self: True if self.available_qty > 0 else False
    )


    def _compute_available_qty(self):
        for rec in self:
            qty = self.env['tr.stock.production.lot'].search_count([
                ('product_id', '=', rec.id),
                ('stage', '=', 'available')
            ])
            rec.available_qty = qty



    def _search_qty_available(self, operator, value):
        products = self.search([]).filtered(lambda self: self.available_qty > value)
        return [('id', 'in', [self.id for self in products] if products else False)]


    def _compute_total_qty(self):
        for rec in self:
            qty = self.env['tr.stock.production.lot'].search_count([
                ('product_id', '=', rec.id),
                ('state', '=', 'done')
            ])
            rec.total_qty = qty


    def _search_total_qty(self, operator, value):
        products = self.search([]).filtered(lambda self: self.total_qty > value)
        return [('id', 'in', [self.id for self in products] if products else False)]


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


