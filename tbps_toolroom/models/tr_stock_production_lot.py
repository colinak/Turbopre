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

class TrStockProductionLot(models.Model):
    _name = 'tr.stock.production.lot'
    _description = 'Toolroom N° de Serie'
    _order = 'name, id'
    _rec_name = 'name'
    
    name = fields.Char(
        string="Nº de serie",
        required=True
    )
    company_id = fields.Many2one(
        "res.company",
        string="Compañia"
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto",
        required=True
    )
    product_uom_id = fields.Many2one(
        "uom.uom",
        string="Unidad de medida"
    )
    product_qty = fields.Integer(
        string="Cantidad"
    )
    # quant_ids = fields.One2many(
        # "tr.stock.quant",
        # "lot_id",
        # string="Cantidades"
    # )
    ref = fields.Char(
        string="Referencia"
    )
    note = fields.Text(
        string="Descripción"
    )
