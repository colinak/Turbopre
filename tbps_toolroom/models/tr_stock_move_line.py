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
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class TrStockMoveLine(models.Model):
    _name = 'tr.stock.move.line'
    _description = 'Toolroom Stock Move line'
    _rec_name = "product_id"
    _order = 'reference'

    
    name = fields.Char(
        string="Descripción"
    )
    reference = fields.Char(
        related="move_id.reference", 
        store=True, 
        related_sudo=False, 
        readonly=False
    )
    company_id = fields.Many2one(
        "res.company", 
        string='Compañia', 
        readonly=True, 
        # required=True, 
        index=True
    )
    move_id = fields.Many2one(
        "tr.stock.move",
        string="Movimiento de stock"
    )
    picking_id = fields.Many2one(
        "tr.stock.picking",
        string="Transferencia",
        check_company=True,
        index=True,
        help='La operación de stock donde se ha realizado el embalaje.'
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto",
        ondelete="cascade", 
        check_company=True, 
        domain="[('type', '!=', 'service')]",
        index=True
    )
    product_uom_category_id = fields.Many2one(
        related="product_id.uom_id.category_id"
    )
    product_uom_id = fields.Many2one(
        "uom.uom", 
        string="Unidad de medida",
        required=True,
        domain="[('category_id', '=', product_uom_category_id)]"
    )
    product_qty = fields.Integer(
        "Cantidad real reservada",
        # digits=0, 
        copy=False,
        # compute='_compute_product_qty', 
        # inverse='_set_product_qty', 
        # store=True
    )
    product_uom_qty = fields.Integer(
        string="Reservado",
        default=1, 
        # digits='Product Unit of Measure', 
        # required=True, 
        # copy=False
    )
    qty_done = fields.Integer(
        string="Hecho",
        default=1,
        # digits='Product Unit of Measure', 
        # copy=False
    )
    lot_id = fields.Many2one(
        "tr.stock.production.lot", 
        string="Númeor de serie",
        domain="[('product_id', '=', product_id), ('company_id', '=', company_id)]", 
        check_company=True
    )
    lot_name = fields.Char('N° de serie')
    date = fields.Datetime(
        string="Fecha",
        default=fields.Datetime.now, 
        required=True
    )
    owner_id = fields.Many2one(
        "res.partner",
        string="Propieratio",
        check_company=True,
        help="Al validar la transferencia, los productos serán tomados de este propietario."
    )
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Desde", 
        check_company=True,
        required=True
    )
    location_dest_id = fields.Many2one(
        "tr.stock.location",
        string="Hasta", 
        check_company=True,
        required=True
    )
    picking_code = fields.Selection(
        string="Code",
        related="picking_id.picking_type_code",
        readonly=True
    )
    state = fields.Selection(
        related="move_id.state",
        store=True,
        related_sudo=False
    )
    description_picking = fields.Text(string="Descripción picking")



    @api.onchange('lot_name')
    def _onchange_lot_name(self):
        if self.lot_name:
            serial_lot = self.env['tr.stock.production.lot'].search([(
                'name', '=', self.lot_name
            )],limit=1)
            if len(serial_lot) < 1:
                raise UserError("Error, No se encontro ninguna herramienta con este número de serie.")
            else:
                self.lot_id = serial_lot.id
                self.product_id = serial_lot.product_id.id
                self.location_id = serial_lot.location_id.id
                self.product_uom_id = serial_lot.product_uom_id.id





