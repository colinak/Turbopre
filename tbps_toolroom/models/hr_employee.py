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



class TpsEmployee(models.Model):
    _inherit = 'tps.employee'


    tools_ids = fields.One2many(
        "tr.stock.production.lot",
        "employee_id",
        string="Equipos/Herramientas",
        # domain="[(stage, '=', 'assigned')]"
    )
    tools_count = fields.Integer(
        string="Herramientas Asignadas",
        compute="_compute_tools_count"
    )
    assignment = fields.Char(
        string="Assignment",
        default="assigned"
    )
    loans = fields.Char(
        string="Loans",
        default="loan"
    )


    @api.depends('tools_ids')
    def _compute_tools_count(self):
        for location in self:
            location.tools_count = len(location.tools_ids)
