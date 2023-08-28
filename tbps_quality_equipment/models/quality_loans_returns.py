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
    deadline = fields.Date(
        string="Fecha de entrega",
        required=True,
    )
    signature_applicant = fields.Char(
        string="Firma solicitante",
        required=True,
    )
    signature_deliverer = fields.Char(
        string="Firma quien entrega",
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
        string="Firma quien recibe"
    )
    signature_deliverer2 = fields.Char(
        string="Firma quien entrega"
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


    # project = fields.Char(string="Project")
    # services_order = fields.Char(string="Services Order")
    # location = fields.Char(string="Location")
