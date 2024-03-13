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

class TrStockMove(models.Model):
    _name = 'tr.stock.move'
    _description = 'Toolroom Stock Move'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char('Descripción', index=True, required=True)
    date = fields.Datetime(
        'Fecha programada', 
        default=fields.Datetime.now,
        index=True, 
        required=True,
        help="Fecha programada hasta que se realiza el movimiento, luego fecha de procesamiento del movimiento real"
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto",
        domain="[('type', 'in', ['product', 'consu'])]", 
        index=True,
        required=True,
        states={'done': [('readonly', True)]}
    )
    description_picking = fields.Text('Descripción del Picking')
    product_qty = fields.Integer(
        'Cantidad real', 
        # compute='_compute_product_qty',
        # inverse='_set_product_qty',
        # digits=0, 
        # store=True, 
        # compute_sudo=True,
        help='Cantidad en la UM por defecto del producto'
    )
    qty_done = fields.Integer(
        string="Hecho",
        # default=1,
        # digits='Product Unit of Measure', 
        # copy=False
    )
    product_availability = fields.Integer(
        "Cantidad disponible",
        related="product_id.available_qty",
        # compute='_compute_product_qty', 
        # store=True, 
        help='Cantidad disponible del producto'
    )
    availability = fields.Integer(
        string="Cantidad pronosticada"
    )
    date_deadline = fields.Datetime(
        string="Fecha límite"
    )
    delay_alert_date = fields.Datetime(
        string="Fecha de alerta de retraso"
    )
    description_picking = fields.Text(
        string="Descripción de Picking"
    )
    inventory_id = fields.Many2one(
        "tr.stock.inventory",
        string="Inventario"
    )
    location_dest_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación destino"
    )
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación origen"
    )
    lot_ids = fields.Many2many(
        "tr.stock.production.lot",
        "move_id",
        "lot_id",
        "tr_stock_move_production_lot_rel",
        string="Números de serie"
    )
    lot_name = fields.Char('N° de serie')
    move_dest_ids = fields.Many2many(
        "tr.stock.move",
        "move_orig_id",
        "move_dest_id",
        "tr_stock_move_move_rel",
        string="Movimientos de destino"
    )
    move_line_ids = fields.One2many(
        "tr.stock.move.line",
        "move_id",
        string="Apuntes"
    )
    note = fields.Text(
        string="Notas"
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Dirección de destino"
    )
    picking_code = fields.Selection(
        string="Code",
        related="picking_id.picking_type_code"
    )
    picking_id = fields.Many2one(
        "tr.stock.picking",
        string="Transferir"
    )
    picking_partner_id = fields.Many2one(
        "res.partner",
        string="Transferir"
    )
    reserved_availability = fields.Integer(
        string="Cantidad Reservada",
        dafault=0
    )
    product_tmpl_id = fields.Many2one(
        "product.template",
        string="Plantilla de producto"
    )
    product_type = fields.Selection(
        string="Tipo de producto",
        related="product_id.type"
    )
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id')
    product_uom_qty = fields.Integer(
        string="Demanda",
        default=0
    )
    product_uom = fields.Many2one(
        "uom.uom",
        string="Unidad de medida",
        domain="[('category_id', '=', product_uom_category_id)]"
    )
    reference = fields.Char(
        string="Referencia",
        # compute='_compute_reference', 
        store=True
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Nuevo'),
            ('done', 'Realizado'),
            ('cancel', 'Cancelada'),
        ],
        string="Estado"
    )


    # @api.depends('product_id', 'product_uom', 'product_uom_qty')
    # def _compute_product_qty(self):
        # rounding_method = 'HALF-UP'
        # for move in self:
            # move.product_qty = move.product_uom._compute_quantity(
                # move.product_uom_qty,
                # move.product_id.uom_id,
                # rounding_method=rounding_method
            # )

