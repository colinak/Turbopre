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

class TrStockWarehouse(models.Model):
    _name = 'tr.stock.warehouse'
    _description = 'Toolroom Warehouse'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Almacén",
        index=True,
        required=True
    )
    code = fields.Char(
        string="Nombre corto",
        required=True, 
        size=5, 
        help="Nombre abreviado utilizado para identificar su almacén"
    )
    active = fields.Boolean('Activo?', default=True)
    virtual_location_id = fields.Many2one(
        'tr.stock.location', 
        'Virtual Location',
        # domain="[('usage', '=', 'virtual'), ('company_id', '=', company_id)]",
        # required=True
    )
    company_id = fields.Many2one(
        'res.company', 
        'Compañia', 
        default=lambda self: self.env.company,
        index=True, 
        readonly=True, 
        required=True,
        help='La empresa se configura automáticamente a partir de sus preferencias de usuario.'
    )
    partner_id = fields.Many2one(
        'res.partner',
        'Dirección',
        default=lambda self: self.env.company.partner_id,
        check_company=True
    )
    lot_stock_id = fields.Many2one(
        'tr.stock.location', 
        string="Ubicación de Stock",
        required=True, 
    )
    sequence = fields.Integer(
        default=10,
        help="Da la secuencia de esta línea al mostrar los almacenes."
    )
    note = fields.Text(
        string="Notas",
        help="Esta nota es solo para fines internos."
    )
    _sql_constraints = [
        ('warehouse_name_uniq', 'unique(name, company_id)', '¡El nombre del almacén debe ser único por empresa!'),
        ('warehouse_code_uniq', 'unique(code, company_id)', '¡El nombre abreviado del almacén debe ser único por empresa!'),
    ]


    
    @api.model
    def create(self, vals):
        vals['virtual_location_id'] = self.env['tr.stock.location'].create(
            {'name': vals.get('code'), 'usage': 'virtual', 'active': True}
        ).id
        vals['lot_stock_id'] = self.env['tr.stock.location'].create(
            {'name': 'Stock', 'location_id': vals.get('virtual_location_id'), 'usage': 'internal', 'active': True}
        ).id
        warehouse = super(TrStockWarehouse, self).create(vals)

        return warehouse


    def write(self, vals):
        if vals.get('code'):
            new_code = vals.get('code')
            virtual_location_id = self.virtual_location_id.id
            virtual_location = self.env['tr.stock.location'].browse(virtual_location_id)
            for vl in virtual_location:
                vl.write({'name': new_code})
        warehouse = super(TrStockWarehouse, self).write(vals)
            
