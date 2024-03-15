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


    quality_work_location_id = fields.Many2one(
        "quality.location",
        string="Ubicación de trabajo",
        help="Ubicación de trabajo"
    )
    quality_equipment_ids = fields.One2many(
        "quality.equipment",
        "employee_assigned_id",
        string="Equipos Asignados",
        help="Listado de Equipos"
    )
    quality_equipment_count = fields.Integer(
        string="Equipos Asignados",
        compute="_compute_quality_equipment_count"
    )


    @api.depends('quality_equipment_ids')
    def _compute_quality_equipment_count(self):
        for location in self:
            location.quality_equipment_count = len(location.quality_equipment_ids)





