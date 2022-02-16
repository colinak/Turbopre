#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

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
        string="Enter Certificador",
        help="Enter Certificador"
    )
    type_activity_id = fields.Many2one(
        'quality.activity.type',
        string="Type Activity",
        required=True,
        help="Type of action to execute"
    )
    date_execute = fields.Date(
        string="Date Execute",
        required=True,
    )
    date_expiration = fields.Date(
        string="Expiration Date",
    )
    final_condition_id = fields.Many2one(
        'quality.status',
        string="Final Condition",
        required=True,
    )
    made_by = fields.Char(
        string="Made by",
        required=True,
    )
    certificate_no = fields.Char(string="Certificate Number")
    certificate = fields.Binary(string="Certificado")
    note = fields.Text(string="Observations")
    Certificate_doc = fields.Char(string="Adjuntar Certificado")


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
        if self.final_condition_id.name == 'Dañado':
            self.date_expiration = False
        elif self.final_condition_id.name == 'Equipo Obsoleto Solo de Uso Referencial':
            self.date_expiration = False
