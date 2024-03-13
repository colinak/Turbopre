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
from odoo.exceptions import UserError
_logger = logging.getLogger(__name__)


class TrStockLocation(models.Model):
    _name = "tr.stock.location"
    _description = "Inventory Locations"
    _parent_name = "location_id"
    # _parent_store = True
    _order = 'complete_name'
    _rec_name = 'complete_name'


    name = fields.Char('Location Name', required=True)
    location_id = fields.Many2one(
        'tr.stock.location',
        string="Parent location",
        domain="[('company_id', 'in', [company_id, False])]",
        help="La ubicación Principal, que incluye esta ubicación"
    )
    child_ids = fields.One2many('tr.stock.location', 'location_id', 'Contains')
    complete_name = fields.Char(
        "Full Location Name",
        compute='_compute_complete_name',
        recursive=True, store=True
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
    company_id = fields.Many2one(
        'res.company',
        'Company',
        default=lambda self: self.env.company, index=True,
        help='Let this field empty if this location is shared between companies'
    )
    scrap_location = fields.Boolean(
        '¿Es una ubicación de chatarra?',
        default=False,
        help='Check this box to allow using this location to put scrapped/damaged goods.'
    )
    warehouse_id = fields.Many2one(
        'tr.stock.warehouse',
        string=u"Almacén"
        # compute='_compute_warehouse_id'
    )
    comment = fields.Text(
        string="Notas"
    )
    default_location = fields.Boolean(
        "Ubicación stock predeterminada",
        default=False
    )
    inventory_id = fields.Many2one(
        "tr.stock.inventory",
        string="Inventario"
    )
    prod_lot_id = fields.One2many(
        "tr.stock.production.lot",
        "location_id",
        string="Serial Producto"
    )
    product_serial_count = fields.Integer(
        string="Herramientas",
        compute="_compute_tools_count"
    )


    @api.depends('name', 'location_id.complete_name', 'usage')
    def _compute_complete_name(self):
        for location in self:
            if location.location_id and location.usage != 'view':
                location.complete_name = '%s/%s' % (location.location_id.complete_name, location.name)
            else:
                location.complete_name = location.name

    
    @api.onchange('usage')
    def _onchange_usage(self):
        if self.usage not in ('internal', 'inventory'):
            self.scrap_location = False


    @api.model
    def create(self, vals):
        if vals.get('default_location') == True:
            location = self.env['tr.stock.location'].search([
                ('default_location', '=', True)
            ],limit=1)
            if location:
                msj = """Ya existe una ubicación de stock predeterminada por
                defecto, intente desactivar la que ya existe y regrese aquí
                para activar esta ubicación como ubicación stock predeterminada.
                """
                raise UserError(msj)

        res = super(TrStockLocation, self).create(vals)
        return res



    def write(self, vals):
        if vals.get('default_location') == True:
            location = self.env['tr.stock.location'].search([
                ('default_location', '=', True)
            ],limit=1)
            if location:
                msj = """Ya existe una ubicación de stock predeterminada por
                defecto, intente desactivar la que ya existe y regrese aquí
                para activar esta ubicación como ubicación stock predeterminada.
                """
                raise UserError(msj)

        res = super(TrStockLocation, self).write(vals)
        return res


