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

class TrStockQuant(models.Model):
    _name = 'tr.stock.quant'

    
    name = fields.Char(
        string="Nombre",
        required=True
    )
    product_id = fields.Many2one(
        "product.product",
        string="Herramienta/Equipo",
        required=True
    )
    product_tmpl_id = fields.Many2one(
        "product.template",
        string="Herramienta/Equipo",
    )
    product_uom_id = fields.Many2one(
        "uom.uom",
        string="Unidad de medida"
    )
    company_id = fields.Many2one(
        "res.company",
        string="Compañia"
    )
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Lugar",
        required=True
    )
    lot_id = fields.Many2one(
        "tr.stock.production.lot",
        string="N° de serie",
        required=True
    )
    in_date = fields.Datetime(
        string="Fecha de entrada"
    )
    inventory_quantity = fields.Integer(
        string="Cantidad inventariada"
    )
    available_quantity = fields.Integer(
        string="Cantidad disponible"
    )
    on_hand = fields.Integer(
        string="A mano",
        related="product_id.total_qty"
    )
    employee_id = fields.Many2one(
        "hr.employee",
        string="Empleado"
    )
    quantity = fields.Integer(
        string="Cantidad"
    )

    


