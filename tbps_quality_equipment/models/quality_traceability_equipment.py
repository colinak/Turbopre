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
from dateutil.relativedelta import relativedelta
_logger = logging.getLogger(__name__)


class QualityTraceabilityEquipment(models.Model):
    _name = 'quality.traceability.equipment'
    _description = 'Aquality Traceability Equipment'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="Description")
    equipment_id = fields.Many2one(
        'quality.equipment',
        string="Equipment"
    )
    partner_id = fields.Many2one(
        'res.partner',
        string="Ente Certificador",
        domain="[('supplier', '=', True)]",
        help="Ente Certificador"
    )
    type_activity_id = fields.Many2one(
        'quality.activity.type',
        string="Type Activity",
        required=True,
        help="Type of action to execute"
    )
    clasification = fields.Selection(
        [
            ('follow-up', 'SEGUIMIENTO'),
            ('measurement', 'MEDICIÓN'),
        ],
        string="Clasificación",
    )
    date_execute = fields.Date(
        string="Date Execute",
        required=True,
    )
    date_expiration = fields.Date(
        string="Expiration Date",
        required=True,
    )
    final_condition_id = fields.Many2one(
        'quality.status',
        string="Final Condition",
        required=True,
    )
    made_by = fields.Char(
        string="Made by",
    )
    certificate_no = fields.Char(string="Certificate Number")
    certificate = fields.Binary(string="Certificado")
    certificate_name = fields.Char(string="File Name")
    note = fields.Text(string="Observations")
    Certificate_doc = fields.Char(string="Adjuntar Certificado")
    active = fields.Boolean(string="Archived", default=True)


    @api.onchange('date_execute')
    def _onchange_date_execute(self):
        if self.date_execute and self.equipment_id.frequency_cal_ver != 0:
            expired_date = (
                fields.Datetime.from_string(self.date_execute) + 
                relativedelta(months=int(self.equipment_id.frequency_cal_ver))
            )
            self.date_expiration = expired_date

    
    @api.onchange('final_condition_id')
    def _onchange_final_condition(self):
        if self.final_condition_id.name == 'DAÑADO':
            self.date_expiration = False
        elif self.final_condition_id.name == 'EQUIPO OBSOLETO SSOLO DE USO REFERENCIAL':
            self.date_expiration = False


