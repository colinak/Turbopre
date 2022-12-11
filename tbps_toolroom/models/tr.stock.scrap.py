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

class TrStockScrap(models.Model):
    _name = 'tr.stock.scrap'
    _description = 'Toolroom Scrap'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="Referencia", required=True)
    # date_done = fields.Date(
        # string="Fecha"
    # )
    # location_id = fields.Many2one(
        # "tr.stock.location",
        # string="Ubicación origen"
    # )
    # lot_id = fields.Many2one(
        # "tr.stock.production.lot",
        # string="N° de serie"
    # )
    # move_id = fields.Many2one(
        # "tr.stock.move",
        # string="Movimiento desecho"
    # )
    # owner_id = fields.Many2one(
        # "res.partner",
        # string="Propietario"
    # )
    # product_id = fields.Many2one(
        # "product.product",
        # string="Producto"
    # )
    # product_uom_category_id = fields.Many2one(
        # "uom.category",
        # string="Categoría"
    # )
    # product_uom_id = fields.Many2one(
        # "uom.uom",
        # string="Unidad de medida"
    # )
    # scrap_location_id = fields.Many2one(
        # "tr.stock.location",
        # string="Ubicación de desecho"
    # )
    # scrap_qty = fields.Integer(
        # string="Cantidad"
    # )
    # state = fields.Selection(
        # selection=[
            # ('draft', 'Borrador'),
            # ('done', 'Realizado'),
        # ],
        # string="Estado"
    # )




