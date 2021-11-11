#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)


class QualityActivityType(models.Model):
    _name = 'quality.activity.type'
    _description = 'Aquality Traceability Equipment'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="name", required=True)
    type_of_notification = fields.Selection(
        [('alert', 'Alert'), ('error', 'Error')],
        string="Type de decoration"
    )
    responsible_id = fields.Many2one(
        'hr.employee',
        string="Responsible",
        help="Empleado responsable"
    )
    description = fields.Html(string="Description")

