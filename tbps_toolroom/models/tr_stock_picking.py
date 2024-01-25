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

class TrStockPicking(models.Model):
    _name = 'tr.stock.picking'
    _description = 'Toolroom Operaciones'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Referencia",
        required=True,
        copy=False, 
        readonly=True, 
        index=True, 
        default=lambda self: _('Nuevo')
    )
    company_id = fields.Many2one(
        "res.company",
        string="Compañia"
    )
    date = fields.Datetime(
        string="Fecha",
        default=fields.Datetime.now, 
        index=True, 
        required=True,
        help="Fecha programada hasta que se realiza el movimiento, luego fecha de procesamiento del movimiento real"
    )
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación origen",
        # required=True
    )
    location_dest_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación destino",
        # required=True
    )
    move_lines = fields.One2many(
        "tr.stock.move",
        "picking_id",
        string="Movimientos de stock"
    )
    move_line_ids = fields.One2many(
        "tr.stock.move.line",
        "picking_id",
        string="Operaciones"
    )
    picking_type_code = fields.Selection(
        selection=[
            ('assignment', 'Asignación'),
            ('discard', 'Desechar'),
            ('loans', 'Prestamo'),
            ('reception', 'Recepción'),
            ('transfers', 'Transferencias')
        ],
        string='Tipo de Operación',
        required=True,
        default="loans"
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto"
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
    signature_applicant = fields.Char(
        string="PIN Solicitante"
    )
    applicant_id = fields.Many2one(
        "tps.employee",
        string="Solicitante",
        ondelete="RESTRICT"
    )
    signature_deliverer = fields.Char(
        string="PIN quien Entrega"
    )
    delivery_id = fields.Many2one(
        "tps.employee",
        string="Entrega",
        ondelete="RESTRICT"
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('done', 'Validado'),
            ('cancel', 'Cancelado'),
        ],
        string="Estado",
        default="draft"
    )
    # active = fields.Boolenam("Activo")



    @api.onchange('signature_applicant')
    def _onchange_signature_applicant(self):
        if self.signature_applicant:
            applicant = self.env['tps.employee'].search(
                [('pin', '=', self.signature_applicant)],
                limit=1
            )
            if applicant:
                self.applicant_id = applicant.id
            else:
                self.applicant_id = ""
                raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")



    @api.onchange('signature_deliverer')
    def _onchange_deliverer_signature(self):
        if self.signature_deliverer:
            deliverer = self.env['tps.employee'].search(
                [('pin', '=', self.signature_deliverer)],
                limit=1
            )
            if deliverer:
                self.delivery_id = deliverer.id
            else:
                self.delivery_id = ""
                raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")


    @api.model
    def create(self, vals):
        if vals.get('name', _('Nuevo')) == _('Nuevo'):
            if vals.get('picking_type_code') == "assignment":
                vals['name'] = self.env['ir.sequence'].next_by_code('tr.stock.picking.assignment') or _('Nuevo')
            elif vals.get('picking_type_code') == "loans":
                vals['name'] = self.env['ir.sequence'].next_by_code('tr.stock.picking.loans') or _('Nuevo')
            elif vals.get('picking_type_code') == "reception":
                vals['name'] = self.env['ir.sequence'].next_by_code('tr.stock.picking.returns') or _('Nuevo')
            elif vals.get('picking_type_code') == "Transfers":
                vals['name'] = self.env['ir.sequence'].next_by_code('tr.stock.picking.transfers') or _('Nuevo')
        res = super(TrStockPicking, self).create(vals)
        return res



    def action_validate(self):
        pass



    def action_cancel_draft(self):
        pass






