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

class TrProductTemplate(models.Model):
    _inherit = 'product.template'


    type = fields.Selection(selection_add=[
            ('product', 'Almacenable')
        ], 
        tracking=True, 
        default="product",
        ondelete={'product': 'set default'}
    )
    available_qty = fields.Integer(
        "Cantidad Disponible",
        compute='_compute_available_qty',
        # search='_search_qty_available',
        # compute_sudo=False, 
        # digits='Product Unit of Measure'
    )
    total_qty = fields.Integer(
        "Cantidad Disponible",
        compute='_compute_total_qty',
        # search='_search_qty_available',
        # compute_sudo=False, 
        # digits='Product Unit of Measure'
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
        for template in self:
            if len(template.product_variant_ids) > 1:
                for variants in template.product_variant_ids:
                    template.available_qty += variants.available_qty
            else:
                template.available_qty = template.product_variant_id.available_qty


    def _compute_total_qty(self):
        for template in self:
            if len(template.product_variant_ids) > 1:
                for variants in template.product_variant_ids:
                    template.total_qty += variants.total_qty
            else:
                template.total_qty = template.product_variant_id.total_qty



    def action_open_total_quants(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("tbps_toolroom.action_tr_stock_quant")
        action['domain'] = [('product_id.product_tmpl_id', 'in', self.ids)]
        return action


    def action_open_available_quants(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("tbps_toolroom.action_tr_stock_production_lot")
        action['domain'] = [
            ('product_id.product_tmpl_id', 'in', self.ids), 
            ('state', '=', 'done'),
            ('stage', '=', 'available'),
        ]
        return action


    def action_view_tr_stock_move_lines(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("tbps_toolroom.tr_stock_move_line_action")
        action['domain'] = [('product_id.product_tmpl_id', 'in', self.ids)]
        return action

