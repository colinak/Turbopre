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
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="Description")
    equipment_id = fields.Many2one(
        'quality.equipment',
        string="Equipo",
        required=True,
        domain="[('stage', '=', 'available')]"
    )
    code = fields.Char(
        string="Código",
        required=True,
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
        # related="equipment_id.status_id"
    )
    applicant_id = fields.Many2one(
        "tps.employee",
        string="Solicitante",
        required=True,
    )
    delivery_id = fields.Many2one(
        "tps.employee",
        string="Entrega",
        required=True,
    )
    deadline = fields.Date(
        string="Fecha de entrega",
        required=True,
    )
    signature_applicant = fields.Char(
        string="PIN solicitante",
        required=True,
    )
    signature_deliverer = fields.Char(
        string="PIN quien entrega",
        required=True,
    )
    entry_date = fields.Date(
        string="Fecha de entrada"
    )
    equipment_status_entry_id = fields.Many2one(
        "quality.status",
        string="Condición del equipo"
    )
    receipt_signature = fields.Char(
        string="PIN quien recibe"
    )
    signature_deliverer2 = fields.Char(
        string="PIN quien devuelve"
    )

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
                    self.equipment_status_id = equipment.status_id.id


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
                    
                



    # project = fields.Char(string="Project")
    # services_order = fields.Char(string="Services Order")
    # location = fields.Char(string="Location")
