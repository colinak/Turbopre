#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
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
    type_activity = fields.Many2one(
        'quality.activity.type',
        string="Type Activity",
        help="Type of action to execute"
    )
    date_execute = fields.Date(
        string="Date Execute"
    )
    date_expiration = fields.Date(
        string="Expiration Date"
    )
    final_condition = fields.Many2one(
        'quality.status',
        string="Final Condition"
    )
    partner_id = fields.Many2one(
        'res.partner',
        string="Made by"
    )
    certificate_no = fields.Char(string="Certificate Number")
    note = fields.Text(string="Observations")
