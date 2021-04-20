#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'
    _description = 'Equipment'

    # @api.onchange('category_id')
    # def _onchange_category_id(self):
        # if self.category_id:
            # self.department_id = self.technician_user_id.depto_responsible_id

    depto_responsible_id = fields.Many2one(
        'hr.department',
        string="Depto Responsible",
        help="Department Responsible for Equipment"
    )

