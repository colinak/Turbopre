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
_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    tools_ids = fields.One2many(
        "tr.stock.production.lot",
        "employee_id",
        string="Equipos Asignados",
        help="Listado de Equipos"
    )
    tools_count = fields.Integer(
        string="Herramientas Asignadas",
        compute="_compute_tools_count"
    )
    tools_work_location_id = fields.Many2one(
        "hr.department",
        string="Ubicación de trabajo",
        help="Ubicación de trabajo"
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
        for res in self:
            res.tools_count = len(res.tools_ids)


    @api.onchange('job_id')
    def _onchange_work_location(self):
        if self.job_id:
            self.tools_work_location_id = self.job_id.department_id


