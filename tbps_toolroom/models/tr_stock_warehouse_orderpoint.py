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

class TrStockWarehouseOrderpoint(models.Model):
    _name = 'tr.stock.warehouse.orderpoint'
    _description = "Reposición"
    _order = 'id desc'

    
    name = fields.Char(
        string="Reference",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('Nuevo')
    )
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación",
        required=True,
        domain="[('default_location', '=', True)]",
        help="Lugar donde se ubicara la herramienta"
    )
    date = fields.Datetime(
        string="Fecha",
        default=fields.Datetime.now,
        index=True,
        required=True,
        readonly=True,
        help="Fecha programada hasta que se realiza el movimiento, luego fecha de procesamiento del movimiento real"
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
    lot_ids = fields.Many2many(
        "tr.stock.production.lot",
        "tr_stock_production_lot_tr_warehouse_ordenpoint_rel",
        "tr_stock_warehouse_orderpoint_id",
        "tr_stock_production_lot_id",
        string="Números de Serie",
        domain="[('stage', '=', ['discarded', 'fault', 'loss']), ('state', '=', 'cancel')]",
        required=True,
        help="Números de serie del equipo o herramienta"
    )
    document = fields.Binary(
        string="Adjuntar documento",
    )
    file_name = fields.Char(string="File name")
    count_line = fields.Integer(
        string="Lineas de Herramientas",
        compute="_compute_count_line"
    )
    notes = fields.Html(string="Notas")


    def _compute_count_line(self):
        for line in self:
            if len(line.lot_ids) > 0:
                line.count_line = len(line.lot_ids)
            else:
                line.count_line = 0


    def action_confirme(self):
        today = fields.Date.context_today(self)
        try:
            for lot in self.lot_ids:
                if lot.stage != 'discarded' and lot.state != 'cancel':
                    raise UserError ("No puede reponer una herramienta que no este desechada")
                else:
                    location = self.env['tr.stock.location'].search([
                        ('default_location', '=', True)
                    ],limit=1)
                    lot.write({
                        'state': "done",
                        'stage': "available",
                        'location_id': location.id,
                        'reentry_date': today
                    })
                self.write({'stage': "done"})
                self.name = self.env['ir.sequence'].next_by_code('tr.stock.warehouse.orderpoint') or _('Nuevo')
        except:
            raise UserError("No se pudo reponer las herramientas.")
