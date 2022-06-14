#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class TrStockPickingType(models.Model):
    _inherit = 'stock.picking.type'
    _name = 'tr.stock.picking.type'
    _description = 'Toolroom Tipo de Operacion'
    _order = 'name'
    _rec_name = 'name'


    sequence_id = fields.Many2one(
        'ir.sequence', 
        string='Reference Sequence',
        check_company=True,
        copy=False
    )
    warehouse_id = fields.Many2one(
        'tr.stock.warehouse',
        string="Almacén",
        ondelete='cascade',
        check_company=True
    )

