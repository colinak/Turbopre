#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class MaintenanceEquipmentCategory(models.Model):
    _inherit = 'maintenance.equipment.category'
    _description = 'Equipment Categories'

    @api.onchange('depto_responsible_id')
    def _onchange_depto_responsible_id(self):
        if self.depto_responsible_id:
            self.technician_user_id = self.depto_responsible_id.manager_id.user_id

    depto_responsible_id = fields.Many2one(
        'hr.department',
        # related="name",
        string="Responsible Department",
        help="Department Responsible for Equipment"
    )


