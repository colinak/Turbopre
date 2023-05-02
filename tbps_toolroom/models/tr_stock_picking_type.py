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

class TrStockPickingType(models.Model):
    _name = 'tr.stock.picking.type'
    _description = 'Toolroom Tipo de Operacion'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char('Nombre de operación', required=True)
    color = fields.Integer('Color')
    sequence = fields.Integer(
        'Sequence',
        help="Used to order the 'All Operations' kanban view"
    )
    sequence_code = fields.Char('Code', required=True)
    default_location_src_id = fields.Many2one(
        'tr.stock.location', 
        "Ubicación de origen predeterminada",
        check_company=True,
        help="Esta es la ubicación de origen predeterminada cuando crea un picking manualmente con este tipo de operación. ")
    default_location_dest_id = fields.Many2one(
        'tr.stock.location',
        "Ubicación destino prederterminada",
        check_company=True,
        help="Esta es la ubicación destino predeterminada cuando crea un picking manualmente con este tipo de operación. ")
    code = fields.Selection(
        selection=[
            ('assignment', 'Asignación'),
            ('loans', 'Prestamo'),
            ('reception', 'Recepción'),
            ('transfers', 'Transferencias')
        ],
        string='Tipo de Operación',
        required=True
    )
    warehouse_id = fields.Many2one(
        'tr.stock.warehouse',
        string="Almacén",
        ondelete='cascade',
        check_company=True
    )
    active = fields.Boolean('Activo?', default=True)
    company_id = fields.Many2one(
        'res.company',
        'Compañia',
        required=True,
        default=lambda s: s.env.company.id, index=True
    )
