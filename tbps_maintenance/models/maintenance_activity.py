#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    
    maintenance_activity_id = fields.Many2one(
        'maintenance.activity',
        string="Nombre de Actividad",
        help="Actividad de Mantenimiento a Realizar."
    )

    @api.onchange('maintenance_activity_id')
    def _onchange_maintenance_activity_id(self):
        if self.maintenance_activity_id:
            self.name = self.maintenance_activity_id.name


class MaintenanceActivity(models.Model):
    _name = 'maintenance.activity'
    _description = 'Maintenance Activity'
    _order = 'name'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Activo?")


