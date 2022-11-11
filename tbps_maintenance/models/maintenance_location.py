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


class MaintenanceLocation(models.Model):
    _name = 'maintenance.location'
    _description = 'Ubacación de Mantenimiento'
    _order = 'name'
    _rec_name = 'complete_name'


    name = fields.Char(
        string="Nombre",
        required=True
    )
    complete_name = fields.Char('Nombre Completo', compute='_compute_complete_name', recursive=True, store=True)
    parent_id = fields.Many2one(
        "maintenance.location",
        string="Ubicación padre"
    )
    child_id = fields.One2many(
        "maintenance.location",
        'parent_id',
        string='Categorías hijos'
    )
    type_location = fields.Selection(
        selection=[
            ('internal', 'Ubicacion interna'),
            ('external', 'Ubicacion externa'),
            ('supplier', 'Ubicacion de proveedor'),
            ('customer', 'Ubicacion de cliente'),
            ('transit', 'Ubicacion de tránsito'),
            ('inventory', 'Perdida de inventario')
        ],
        string="Tipo de ubicación",
        default='internal',
        help="Seleccione el tipo de ubicación",
    )
    scrap_location = fields.Boolean(
        string="¿Es una ubicación de chatarra?"
    )
    note = fields.Text(string="Notas")
    active = fields.Boolean(string="Activo?", default=True)
    responsible_id = fields.Many2one(
        "hr.employee",
        string="Responsable"
    )


    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for location in self:
            if location.parent_id:
                location.complete_name = '%s / %s' % (location.parent_id.complete_name, location.name)
            else:
                location.complete_name = location.name
