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

class TrStockInventory(models.Model):
    _name = 'tr.stock.inventory'
    _description = 'Toolroom Inventario'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Nombre",
        default="Inventario",
        required=True,
        states={'draft': [('readonly', False)]}
    )
    date = fields.Date(
        string="Fecha de inventario",
        readonly=True,
        default=fields.Datetime.now,
    )
    location_ids = fields.One2many(
        "tr.stock.location",
        "inventory_id",
        string=u"Ubicaciones",
        states={'done': [('readonly', True)]}
    )
    line_ids = fields.One2many(
        "tr.stock.inventory.line",
        "inventory_id",
        string="Lineas de Inventario",
        states={'done': [('readonly', True)]}
    )
    product_ids = fields.One2many(
        "product.product",
        "inventory_id",
        string="Productos"
    )
    # move_ids = fields.One2many(
        # "tr.stock.move",
        # "inventory_id",
        # string="Movimientos creados",
        # states={'done': [('readonly', True)]}
    # )
    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('cancel', 'Cancelada'),
            ('confirm', 'En Progreso'),
            ('done', 'Validado'),
        ],
        string="Stado"
    )


    def action_start(self):
        pass


    def action_open_inventory_lines(self):
        pass




class TrStockInventoryLine(models.Model):
    _name = 'tr.stock.inventory.line'
    _description = 'Toolroom Linea de Inventario'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Nombre"
    )
    inventory_id = fields.Many2one(
        "tr.stock.inventory",
        string="Inventario"
    )
    difference_qty = fields.Integer(
        string="Diferencia"
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Propietario"
    )
    product_lot_id = fields.Many2one(
        "tr.stock.production.lot",
        string="N° de Serie"
    )
    product_qty = fields.Integer(
        string="Cantidad"
    )
    product_uom_id = fields.Many2one(
        "uom.uom",
        string="Unidad de medida"
    )
    inventory_id = fields.Many2one(
        "tr.stock.inventory",
        string="Inventario"
    )
