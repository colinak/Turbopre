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
import time
import logging
_logger = logging.getLogger(__name__)

class TrStockMoveLine(models.Model):
    _name = 'tr.stock.move.line'
    _description = 'Toolroom Stock Move line'
    _rec_name = "product_id"
    _order = 'reference, id'

    
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
        copy=False,
    )
    product_uom_qty = fields.Integer(
        string="Reservado",
        default=1,
    )
    qty_done = fields.Integer(
        string="Hecho",
        default=1,
    )
    lot_id = fields.Many2one(
        "tr.stock.production.lot", 
        string="Número de serie",
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
        # required=True
    )
    location_dest_id = fields.Many2one(
        "tr.stock.location",
        string="Hasta", 
        check_company=True,
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
        """Busca el lot_name por texto y auto-completa los datos asociados."""
        if not self.lot_name:
            return

        # 1. Búsqueda óptima del lote
        serial = self.env['tr.stock.production.lot'].search([
            ('name', '=', self.lot_name.strip())
        ], limit=1)

        # 2. Validación de existencia
        if not serial:
            raise UserError(_("¡Error!\nNo se encontró ninguna herramienta con este número de serie."))

        # Variables de control para mejorar la lectura
        picking_type = self.picking_id.picking_type_code
        stage = serial.stage
        
        _logger.info("Procesando serial: %s | Tipo: %s | Estado: %s", self.lot_name, picking_type, stage)

        # 3. Validaciones de Estado de la Herramienta
        if stage != 'available' and picking_type != 'reception':
            raise UserError(_("¡Error!\nEsta herramienta ya se encuentra prestada o no está disponible."))
        if stage == 'available' and picking_type == 'reception':
            raise UserError(_("¡Error!\nEsta herramienta ya está en almacén (no se encuentra prestada)."))

        # 4. Asignación limpia de datos (se ejecuta solo si pasa todas las validaciones)
        self.update({
            'lot_id': serial.id,
            'product_id': serial.product_id.id,
            'location_id': serial.location_id.id,
            'product_uom_id': serial.product_uom_id.id,
            'location_dest_id': (
                serial.default_location_id.id
                if picking_type == 'reception'
                else self.picking_id.location_dest_id.id
            )
        })


