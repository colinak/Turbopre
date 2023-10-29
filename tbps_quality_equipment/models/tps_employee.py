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


    equipment_ids = fields.One2many(
        "quality.equipment",
        "employee_assigned_id",
        string="Equipos Asignados",
        help="Listado de Equipos"
    )
    equipment_count = fields.Integer(
        string="Equipos Asignados",
        compute="_compute_equipment_count"
    )


    @api.depends('equipment_ids')
    def _compute_equipment_count(self):
        for location in self:
            location.equipment_count = len(location.equipment_ids)


