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


class TrStockLocation(models.Model):
    _name = "tr.stock.location"
    _description = "Inventory Locations"
    _parent_name = "location_id"
    _parent_store = True
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
            ('supplier', 'Ubicacion de proveedor'),
            ('customer', 'Ubicacion de cliente'),
            ('transit', 'Ubicacion de tránsito'),
            ('inventory', 'Perdida de inventario')
        ],
        string='Location Type',
        default='internal',
        index=True,
        required=True,
        help="* Vendor Location: Virtual location representing the source location for products coming from your vendors"
             "\n* View: Virtual location used to create a hierarchical structures for your warehouse, aggregating its child locations ; can't directly contain products"
             "\n* Internal Location: Physical locations inside your own warehouses,"
             "\n* Customer Location: Virtual location representing the destination location for products sent to your customers"
             "\n* Inventory Loss: Virtual location serving as counterpart for inventory operations used to correct stock levels (Physical inventories)"
             "\n* Production: Virtual counterpart location for production operations: this location consumes the components and produces finished products"
             "\n* Transit Location: Counterpart location that should be used in inter-company or inter-warehouses operations"
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
    return_location = fields.Boolean(
        '¿Es una ubicación de devolución?',
        help='Check this box to allow using this location as a return location.'
    )
    warehouse_id = fields.Many2one(
        'tr.stock.warehouse', 
        # compute='_compute_warehouse_id'
    )

    @api.depends('name', 'location_id.complete_name', 'usage')
    def _compute_complete_name(self):
        for location in self:
            if location.location_id and location.usage != 'view':
                location.complete_name = '%s/%s' % (location.location_id.complete_name, location.name)
            else:
                location.complete_name = location.name


    # @api.depends('warehouse_view_ids')
    # def _compute_warehouse_id(self):
        # warehouses = self.env['tr.stock.warehouse'].search([('view_location_id', 'parent_of', self.ids)])
        # view_by_wh = OrderedDict((wh.view_location_id.id, wh.id) for wh in warehouses)
        # self.warehouse_id = False
        # for loc in self:
            # path = set(int(loc_id) for loc_id in loc.parent_path.split('/')[:-1])
            # for view_location_id in view_by_wh:
                # if view_location_id in path:
                    # loc.warehouse_id = view_by_wh[view_location_id]
                    # break
    
    @api.onchange('usage')
    def _onchange_usage(self):
        if self.usage not in ('internal', 'inventory'):
            self.scrap_location = False

