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
from dateutil.relativedelta import relativedelta
_logger = logging.getLogger(__name__)

class TrStockProductionLot(models.Model):
    _name = 'tr.stock.production.lot'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Toolroom N° de Serie'
    _order = 'name, id'
    _rec_name = 'name'
    
    name = fields.Char(
        string="Nº de serie",
        required=True,
        tracking=True,
        help="Número de serie de la herramienta."
    )
    company_id = fields.Many2one(
        "res.company",
        string="Compañia"
    )
    default_location_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación predeterminada",
        tracking=True,
        domain="[('usage', '=', 'internal')]",
        help="Ubicación fija donde debe guardarse este equipo cuando no está asignado."
    )
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación actual",
        tracking=True,
    )
    employee_id = fields.Many2one(
        "hr.employee",
        string="Empleado Asignado",
        tracking=True,
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto",
        required=True,
        tracking=True,
    )
    product_uom_id = fields.Many2one(
        "uom.uom",
        string="Unidad de medida",
        related="product_id.uom_id"
    )
    product_qty = fields.Integer(
        string="Cantidad",
        default=1
    )
    quant_ids = fields.One2many(
        "tr.stock.quant",
        "lot_id",
        string="Cantidades"
    )
    ref = fields.Char(
        string="Referencia"
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('done', 'Validado'),
            ('cancel', 'Cancelada'),
        ],
        string="Estado",
        tracking=True,
        default="draft"
    )
    stage = fields.Selection(
        [
            ('available', 'Disponible'),
            ('assigned', 'Asignada'),
            ('loan', 'Prestada'),
            ('reserved', 'Reservada'),
            ('in_custody', 'En Custodia'),
            ('loss', 'Perdida'),
            ('fault', 'Averiada'),
            ('discarded', 'Desechada'),
        ],
        string="Stage",
        tracking=True,
        default='available'
    )
    note = fields.Text(
        string="Descripción"
    )
    assigned_date = fields.Datetime(
        string="Fecha Asignación",
        tracking=True,
        help="Fecha de Asignación de al herramienta"
    )
    scrap_date = fields.Datetime(
        string="Fecha Baja de Inventario",
        tracking=True,
        help="Fecha de Asignación de al herramienta"
    )
    required_certification = fields.Boolean(
        string="Requiere certificación?",
        default=False
    )
    execute_date = fields.Date(
        string="Fecha de certificación"
    )
    expiration_date = fields.Date(
        string="Fecha de expiración"
    )
    certification_frequency = fields.Integer(
        string="Frecuencia de certificación"
    )
    final_condition = fields.Selection(
        selection=[
            ('current', 'Vigente'),
            ('expired', 'Vencido')
        ],
        string="Condición final",
        required=True,
    )
    active = fields.Boolean(
        string="Activo?",
        default=True
    )


    _sql_constraints = [('unique_serial_lot',
            'UNIQUE(name)',
            'El número de serie que intenta registrar ya exitste.'
        )
    ]


    @api.onchange('certification_frequency', 'execute_date')
    def _onchange_calculate_certification_next(self):
        if self.execute_date:
            expiration = int(self.certification_frequency)
            self.expiration_date = fields.Datetime.from_string(
                self.execute_date
            ) + relativedelta(months=expiration)


    @api.onchange('expiration_date')
    def _onchange_certification_status(self):
        today = fields.Date.context_today(self)
        for rec in self:
            # 1. Validación de seguridad: Si no hay fecha de expiración
            if not rec.expiration_date:
                rec.final_condition = 'expired'
                continue
            if today < rec.expiration_date:
                new_status = 'current'
            else:
                new_status = 'expired'

            # Solo escribimos en el campo si el valor ha cambiado
            if rec.final_condition != new_status:
                rec.final_condition = new_status


    @api.onchange('required_certification')
    def _onchange_required_certification(self):
        if not self.required_certification:
            self.certification_frequency = False
            self.execute_date = False
            self.expiration_date = False
            self.final_condition = False

    @api.model
    def _cron_check_expiration(self):
        """ Método para el ir.cron: marca como 'expired' si la fecha actual >= expiration_date """
        today = fields.Date.today()
        # Buscamos registros vigentes que ya deberían estar expirados
        records_to_update = self.search([
            ('final_condition', '=', 'current'),
            ('expiration_date', '<=', today)
        ])
        
        if records_to_update:
            records_to_update.write({'final_condition': 'expired'})
            _logger.info(f"Se actualizaron {len(records_to_update)} registros")



