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

class TrStockProductionLot(models.Model):
    _name = 'tr.stock.production.lot'
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación",
    )
    employee_id = fields.Many2one(
        "hr.employee",
        string="Empleado Asignado"
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto",
        required=True
    )
    product_uom_id = fields.Many2one(
        "uom.uom",
        string="Unidad de medida",
        related="product_id.uom_id"
    )
    product_qty = fields.Integer(
        string="Cantidad",
        default=1
    )
    quant_ids = fields.One2many(
        "tr.stock.quant",
        "lot_id",
        string="Cantidades"
    )
    ref = fields.Char(
        string="Referencia"
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('done', 'Validado'),
            ('cancel', 'Cancelada'),
        ],
        string="Estado",
        default="draft"
    )
    stage = fields.Selection(
        [
            ('available', 'Disponible'),
            ('assigned', 'Asignado'),
            ('loan', 'Prestado'),
            ('reserved', 'Reservado'),
            ('in_custody', 'En Custodia'),
            ('discarded', 'Desechado'),
        ],
        string="Stage",
        default='available'
    )
    note = fields.Text(
        string="Descripción"
    )
    active = fields.Boolean(
        string="Activo?",
        default=True
    )


    _sql_constraints = [('unique_serial_lot',
            'UNIQUE(name)',
            'El número de serie que intenta registrar ya exitste.'
        )
    ]
