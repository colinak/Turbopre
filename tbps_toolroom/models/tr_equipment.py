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

class TrProductTemplate(models.Model):
    _inherit = 'product.template'


    type = fields.Selection(selection_add=[
        ('product', 'Almacenable')
        ], 
        tracking=True, 
        default="product",
        ondelete={'product': 'set default'}
    )
    available_qty = fields.Float(
        "Cantidad a la mano",
        # compute='_compute_quantities', 
        # search='_search_qty_available',
        # compute_sudo=False, 
        # digits='Product Unit of Measure'
    )

