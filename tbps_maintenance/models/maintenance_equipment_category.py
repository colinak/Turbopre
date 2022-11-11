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

class MaintenanceEquipmentCategory(models.Model):
    _inherit = 'maintenance.equipment.category'
    _description = 'Equipment Categories'
    _order = 'name'

    @api.onchange('depto_responsible_id')
    def _onchange_depto_responsible_id(self):
        if self.depto_responsible_id:
            self.technician_user_id = self.depto_responsible_id.manager_id.user_id

    depto_responsible_id = fields.Many2one(
        'hr.department',
        string="Responsible Department",
        help="Department Responsible for Equipment"
    )
    parent_id = fields.Many2one(
        'maintenance.equipment.category',
        string="Categoría Padre",
        help="Categoría Padre",
        index=True,
        ondelete='cascade'
    )
    child_id = fields.One2many(
        'maintenance.equipment.category',
        'parent_id',
        string='Categorías hijos'
    )


