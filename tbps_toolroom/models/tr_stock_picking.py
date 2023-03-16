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
    _name = 'tr.stock.picking'
    _description = 'Toolroom Operaciones'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Nombre"
    )
    company_id = fields.Many2one(
        "res.company",
        string="Compañia"
    )
    date = fields.Date(
        string="Fecha"
    )
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación origen",
        required=True
    )
    location_dest_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación destino",
        required=True
    )
    # move_line_ids = fields.One2many(
        # "tr.stock.move.line",
        # "picking_id",
        # string="Operaciones"
    # )
    # move_lines = fields.One2many(
        # "tr.stock.move",
        # "picking_id",
        # string="Movimientos de stock"
    # )
    picking_type_code = fields.Selection(
        selection=[
            ('assignment', 'Asignación'),
            ('discard', 'Desechar'),
            ('loans', 'Prestamo'),
            ('reception', 'Recepción'),
            ('transfers', 'Transferencias')
        ],
        string='Tipo de Operación',
        required=True
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto"
    )
    employee_id = fields.Many2one(
        "hr.employee",
        string="Empleado",
        required=True
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Contacto"
    )
    user_id = fields.Many2one(
        "res.users",
        string="Usuario"
    )
    note = fields.Text(
        string="Notas"
    )
    # active = fields.Boolenam("Activo")
