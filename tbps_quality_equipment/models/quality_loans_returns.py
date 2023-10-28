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


class QualityLoansReturns(models.Model):
    _name = 'quality.loans.returns'
    _description = 'Loans & Returns'
    _order = 'deadline'
    _rec_name = 'name'


    name = fields.Char(
        string="Referencia", 
        required=True,
        copy=False, 
        readonly=True, 
        index=True, 
        default=lambda self: _('New')
    )
    code = fields.Char(
        string="Código",
        required=True,
    )
    equipment_id = fields.Many2one(
        'quality.equipment',
        string="Equipo",
        required=True,
        compute="_compute_equipment_date",
        domain="[('stage', '=', 'available')]",
        ondelete="RESTRICT"
    )
    rango = fields.Char(
        string="Rango",
        required=True,
        related="equipment_id.rango"
    )
    equipment_status_id = fields.Many2one(
        "quality.status",
        string="Status",
        required=True,
        related="equipment_id.status_id",
        ondelete="RESTRICT"
    )
    stage = fields.Selection(
        [
            ('draft', 'Borrador'),
            ('loan', 'Prestamo'),
            ('done', 'Devolución'),
            ('cancel', 'Cancelado'),
        ],
        string="Stage",
        default='draft'
    )
    applicant_id = fields.Many2one(
        "tps.employee",
        string="Solicitante",
        required=True,
        ondelete="RESTRICT"
    )
    delivery_id = fields.Many2one(
        "tps.employee",
        string="Entrega",
        required=True,
        ondelete="RESTRICT"
    )
    deadline = fields.Datetime(
        string="Fecha de entrega",
        required=True,
        default=fields.Datetime.now,
    )
    signature_applicant = fields.Char(
        string="PIN solicitante",
        required=True,
    )
    signature_deliverer = fields.Char(
        string="PIN quien entrega",
        required=True,
    )
    entry_date = fields.Datetime(
        string="Fecha de entrada",
    )
    equipment_status_entry_id = fields.Many2one(
        "quality.status",
        string="Condición del equipo",
        ondelete="RESTRICT"
    )
    receipt_signature = fields.Char(
        string="PIN quien recibe"
    )
    receipt_id = fields.Many2one(
        "tps.employee",
        string="Recibe",
        ondelete="RESTRICT"
    )
    signature_deliverer2 = fields.Char(
        string="PIN quien devuelve"
    )
    delivery2_id = fields.Many2one(
        "tps.employee",
        string="Devuelve",
        ondelete="RESTRICT"
    )
    location_id = fields.Many2one(
        "quality.location",
        string="Ubicación",
        domain="[('usage', '=', 'internal'), ('scrap_location', '=', False)]",
        help="Ubicación donde sera utilizado el equipo."
    )
    location_return_id = fields.Many2one(
        "quality.location",
        string="Ubicación",
        domain="[('usage', '=', 'internal'), ('scrap_location', '=', False)]",
        help="Ubicación donde sera utilizado el equipo."
    )
    active = fields.Boolean(string="Archived", default=True)


    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Reference must be unique per company!'),
    ]


    def _compute_equipment_date(self):
        for rec in self:
            if rec.code:
                equipment = self.env['quality.equipment'].search(
                    [('code', '=', rec.code)],
                    limit=1
                )
                if equipment:
                    self.equipment_id = equipment.id


    def _compute_delivery(self):
        for rec in self:
            if rec.signature_deliverer:
                employee = self.env['tps.employee'].search(
                    [('pin', '=', rec.signature_deliverer)],
                    limit=1
                )
                if employee:
                    self.applicant_id = employee.id

    @api.onchange('code')
    def _onchange_code(self):
        if self.code:
            equipment = self.env['quality.equipment'].search(
                [('code', '=', self.code)],
                limit=1
            )
            if equipment:
                self.equipment_id = equipment.id
            else:
                self.equipment_id = ""
                self.rango = ""
                self.equipment_status_id = ""


    @api.onchange('signature_deliverer')
    def _onchange_deliverer_signature(self):
        if self.signature_deliverer:
            employee = self.env['tps.employee'].search(
                [('pin', '=', self.signature_deliverer)],
                limit=1
            )
            _logger.info("Employee" + str(employee))
            if employee:
                self.delivery_id = employee.id
            else:
                self.delivery_id = ""
                raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")


    @api.onchange('signature_applicant')
    def _onchange_signature_applicant(self):
        if self.signature_applicant:
            employee = self.env['tps.employee'].search(
                [('pin', '=', self.signature_applicant)],
                limit=1
            )
            if employee:
                self.applicant_id = employee.id
            else:
                self.applicant_id = ""
                raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")

                
    @api.onchange('signature_deliverer2')
    def _onchange_signature_deliverer2(self):
        if self.signature_deliverer2:
            employee = self.env['tps.employee'].search(
                [('pin', '=', self.signature_deliverer2)],
                limit=1
            )
            if employee:
                self.delivery2_id = employee.id
            else:
                self.delivery2_id = ""
                raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")


    @api.onchange('receipt_signature')
    def _onchange_signature_deliverer(self):
        if self.receipt_signature:
            employee = self.env['tps.employee'].search(
                [('pin', '=', self.receipt_signature)],
                limit=1
            )
            if employee:
                self.receipt_id = employee.id
            else:
                self.receipt_id = ""
                raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")


    @api.model
    def create(self, vals):
        today = fields.Date.today()
        if vals.get('deadline'):
            date = fields.Date.from_string(today)

            deadline = fields.Datetime.to_string(
                fields.Datetime.context_timestamp(
                    self, fields.Datetime.from_string(vals.get('deadline'))))[:10]
            deadline = fields.Date.from_string(deadline)
            if deadline > date:
                raise UserError("La Fecha de Entrega no Puede ser Posterior a la Fecha de hoy.")
        if vals.get('code'):
            equipment = self.env['quality.equipment'].search([
                ('code', '=', vals.get('code'))
            ],limit=1)
            if equipment.stage == 'available':
                vals['stage'] = 'loan'
                equipment.write({
                    'stage': 'loan', 
                    'location_id': vals.get('location_id')
                })
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('quality.loans.returns') or _('New')
            else:
                raise UserError("El Equipo que Intenta Prestar no Esta Disponible, Verifíque y Vuelva a Intentar")
        res = super(QualityLoansReturns, self).create(vals)
        return res


    def write(self, vals):
        today = fields.Date.today()
        if vals.get('entry_date'):
            date = fields.Date.from_string(today)

            deadline = fields.Datetime.to_string(
                fields.Datetime.context_timestamp(
                    self, fields.Datetime.from_string(self.deadline)))[:10]
            deadline = fields.Date.from_string(deadline)

            entry_date = fields.Datetime.to_string(
                fields.Datetime.context_timestamp(
                    self, fields.Datetime.from_string(
                        vals.get('entry_date'))))[:10]
            entry_date = fields.Date.from_string(entry_date)

            if entry_date > today:
                raise UserError("La Fecha de Retorno no Puede ser Posterior a la Fecha de hoy.")
            elif entry_date < deadline:
                raise UserError("La Fecha de Retorno no Puede ser Anterior a la Fecha de Entrega.")
            else:
                equipment = self.env['quality.equipment'].search([
                    ('code', '=', self.code)
                ],limit=1)
                equipment.write({
                    'stage': 'available',
                    'location_id': vals.get('location_return_id')
                })
                vals['stage'] = 'done'
        res = super(QualityLoansReturns, self).write(vals)
        return res


