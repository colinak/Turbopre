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
import logging
_logger = logging.getLogger(__name__)

class TrStockScrap(models.Model):
    _name = 'tr.stock.scrap'
    _description = "Chatarra"
    _order = 'id desc'

    name = fields.Char(
        "Reference",
        default=lambda self: _('Nuevo'),
        copy=False, 
        readonly=True, 
        required=True,
        states={'done': [('readonly', True)]}
    )
    origin = fields.Char(string="Documento Origen")
    date_done = fields.Datetime(
        string="Fecha",
        default=fields.Datetime.now, 
        index=True,
        required=True,
        readonly=True,
        help="Fecha programada hasta que se realiza el movimiento, luego fecha de procesamiento del movimiento real"
    )
    type_operation = fields.Selection(
        selection=[
            ('loss', 'Perdida'),
            ('fault', 'Avería'),
        ],
        string="Tipo de Operación",
        help="Seleccione el tipo de operación"
    )
    document = fields.Binary(string="Adjuntar Documento")
    file_name = fields.Char(string="File name")
    lot_tools_ids = fields.One2many(
        "tr.stock.scrap.line",
        "scrap_id",
        string="Linea de Herramientas",
        help="Seleccione el listado de herramientas a desechar"
    )
    stage = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('done', 'Realizado'),
            ('cancel', 'Cancelado')
        ],
        string="Estatus",
        default="draft"
    )
    count_line = fields.Integer(
        string="Lineas de Herramientas",
        compute="_compute_count_line"
    )
    notes = fields.Html(string="Notas")
    # lot_move_tools_ids = fields.Many2many(
        # "tr.stock.production.lot",
        # string="Linea de Herramientas",
    # )
    tools_lot_line_ids = fields.Many2many(
        "tr.stock.production.lot",
        "tr_stock_production_lot_tr_stock_scrap_rel",
        "tr_stock_scrap_id",
        "tr_stock_production_lot_id",
        domain="[('stage', '=', 'available'), ('state', '=', 'done'), ('active', '=', True)]",
        string="Linea de Herramientas",
    )





    def _compute_count_line(self):
        for line in self:
            line.count_line = len(line.tools_lot_line_ids)


    def action_cancel_draft(self):
        pass



    def action_validate(self):
        pass






class TrStockScrapLine(models.Model):
    _name = 'tr.stock.scrap.line'
    _description = "Linea de Chatarra"
    _order = 'id desc'

    name = fields.Char(
        string="REF"
    )
    scrap_id = fields.Many2one(
        "tr.stock.scrap",
        string="Chatarra"
    )
    lot_id = fields.Many2one(
        "tr.stock.production.lot",
        string="°N Serial TPS",
        domain="[('stage', '=', 'available'), ('state', '=', 'done')]",
        help="Seleccione el serial TPS"
    )
    product_id = fields.Many2one(
        "product.product",
        string="Herramienta",
        related="lot_id.product_id",
        store=True,
        help="Seleccione herramienta"
    )
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación origen",
        related="lot_id.location_id",
        store=True,
        help="Seleccione ubicación"
    )
    location_dest_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación destino",
        domain="[('usage', '=', 'inventory'), ('scrap_location', '=', True)]",
        help="Seleccione ubicación destino"
    )
