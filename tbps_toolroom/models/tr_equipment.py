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
        "Cantidad a la mano",
        compute='_compute_qty_available',
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
    # qty_available = fields.Integer(
        # string="Cantidad a Mano"
        # compute='_compute_quantities', 
        # search='_search_qty_available',
        # compute_sudo=False, 
        # digits='Product Unit of Measure'
    # )


    def _compute_qty_available(self):
        for rec in self:
            rec.available_qty = rec.product_variant_ids.lot_ids.search_count([
                ('state', '=', 'done'),
                ('product_id.id', '=', rec.id)
            ])


