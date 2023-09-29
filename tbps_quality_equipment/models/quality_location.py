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
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class QualityLocation(models.Model):
    _name = 'quality.location'
    _description = 'Ubicaciones'
    _rec_name = 'complete_name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True,
        help="Location Name"
    )
    parent_id = fields.Many2one(
        "quality.location",
        string="Parent Location",
        help="Parent Location"
    )

    child_ids = fields.One2many(
        'quality.location', 
        'parent_id', 
        string="Contains"
    )
    complete_name = fields.Char(
        "Full Location Name",
        compute='_compute_complete_name',
        recursive=True, 
        store=True
    )
    active = fields.Boolean(
        'Active',
        default=True,
        help="By unchecking the active field, you may hide a location without deleting it.")
    usage = fields.Selection(
        selection=[
            ('internal', 'Ubicacion interna'),
            ('external', 'Ubicacion externa'),
            ('virtual', 'Ubicacion Virtual'),
            ('supplier', 'Ubicacion de proveedor'),
            ('customer', 'Ubicacion de cliente'),
            ('transit', 'Ubicacion de tránsito'),
            ('inventory', 'Perdida de inventario')
        ],
        string='Location Type',
        default='internal',
        index=True,
        required=True,
        help="* Ubicación interna: ubicaciones físicas dentro de sus propios almacenes"
             "\n* Ubicación externa: ubicaciones físicas fuera de sus propios almacenes"
             "\n* Virtual: ubicación virtual utilizada para crear estructuras jerárquicas para su almacén, agregando sus ubicaciones secundarias; no puede contener productos directamente"
             "\n* Ubicación del proveedor: ubicación virtual que representa la ubicación de origen de los productos que provienen de sus proveedores"
             "\n* Ubicación del cliente: ubicación virtual que representa la ubicación de destino de los productos enviados a sus clientes"
             "\n* Pérdida de inventario: Ubicación virtual que sirve como contraparte para las operaciones de inventario utilizadas para corregir los niveles de existencias (Inventarios físicos)"
             "\n* Ubicación de tránsito: ubicación de contraparte que se debe usar en operaciones entre empresas o entre almacenes"
    )
    scrap_location = fields.Boolean(
        '¿Es una ubicación de chatarra?',
        default=False,
        help='Check this box to allow using this location to put scrapped/damaged goods.'
    )
    comment = fields.Text(
        string="Notas"
    )

    @api.depends('name', 'parent_id.complete_name', 'usage')
    def _compute_complete_name(self):
        for location in self:
            if location.parent_id and location.usage != 'view':
                location.complete_name = '%s/%s' % (location.parent_id.complete_name, location.name)
            else:
                location.complete_name = location.name



