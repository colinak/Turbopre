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


    name = fields.Char(string="Description")
    code = fields.Char(
        string="Código",
        required=True,
    )
    equipment_id = fields.Many2one(
        'quality.equipment',
        string="Equipo",
        required=True,
        compute="_compute_equipment_date",
        # readonly=True,
        domain="[('stage', '=', 'available')]"
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
        related="equipment_id.status_id"
    )
    applicant_id = fields.Many2one(
        "tps.employee",
        string="Solicitante",
        # compute="_compute_applicant",
        # required=True,
    )
    delivery_id = fields.Many2one(
        "tps.employee",
        string="Entrega",
        # compute="_compute_delivery",
        # required=True,
    )
    deadline = fields.Datetime(
        string="Fecha de entrega",
        required=True,
        default=fields.Datetime.now
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
        string="Fecha de entrada"
    )
    equipment_status_entry_id = fields.Many2one(
        "quality.status",
        string="Condición del equipo"
    )
    receipt_signature = fields.Char(
        string="PIN quien recibe"
    )
    receipt_id = fields.Many2one(
        "tps.employee",
        string="Recibe",
    )
    signature_deliverer2 = fields.Char(
        string="PIN quien devuelve"
    )
    delivery2_id = fields.Many2one(
        "tps.employee",
        string="Devuelve",
    )
    active = fields.Boolean(string="Archived", default=True)


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
        for rec in self:
            if rec.code:
                equipment = self.env['quality.equipment'].search(
                    [('code', '=', self.code)],
                    limit=1
                )
                if equipment:
                    self.equipment_id = equipment.id


    @api.onchange('signature_applicant')
    def _onchange_signature_applicant(self):
        for rec in self:
            if rec.signature_applicant:
                employee = self.env['tps.employee'].search(
                    [('pin', '=', self.signature_applicant)],
                    limit=1
                )
                if employee:
                    self.applicant_id = employee.id
                else:
                    raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")


    @api.onchange('signature_deliverer')
    def _onchange_signature_deliverer(self):
        for rec in self:
            if rec.signature_deliverer:
                employee = self.env['tps.employee'].search(
                    [('pin', '=', self.signature_deliverer)],
                    limit=1
                )
                if employee:
                    self.delivery_id = employee.id
                else:
                    raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")
                    
                
    @api.onchange('signature_deliverer2')
    def _onchange_signature_deliverer2(self):
        for rec in self:
            if rec.signature_deliverer2:
                employee = self.env['tps.employee'].search(
                    [('pin', '=', self.signature_deliverer2)],
                    limit=1
                )
                if employee:
                    self.delivery2_id = employee.id
                else:
                    raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")


    @api.onchange('receipt_signature')
    def _onchange_signature_deliverer(self):
        for rec in self:
            if rec.receipt_signature:
                employee = self.env['tps.employee'].search(
                    [('pin', '=', self.receipt_signature)],
                    limit=1
                )
                if employee:
                    self.receipt_id = employee.id
                else:
                    raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")

