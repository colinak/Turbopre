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
        # compute='_compute_quantities', 
        # search='_search_qty_available',
        # compute_sudo=False,
    )
