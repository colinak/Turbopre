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

class TrStockPicking(models.Model):
    _inherit = 'stock.picking'
    # _name = 'tr.stock.picking'
    # _description = 'Toolroom Operaciones'
    # _order = 'name'
    # _rec_name = 'name'

    # warehouse_id = fields.Many2one(
        # 'tr.stock.warehouse', 
        # 'Almacel', 
        # ondelete='cascade',
        # check_company=True
    # )
    employee_id = fields.Many2one(
        "hr.employee",
        string="Empleado"
    )
