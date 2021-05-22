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

    brand_id = fields.Many2one(
        'maintenance.manufacturers',
        string="Make",
        help="Make Equipment"
    )
    depto_responsible_id = fields.Many2one(
        'hr.department',
        string="Depto Responsible",
        help="Department Responsible for Equipment"
    )
    state = fields.Selection(
        [
            ('available', 'Available'),
            ('assigned', 'Assigned'),
            ('discarded', 'Discarded'),
        ],
        string="Status",
        default="available",
        help="Status"
    )
    other = fields.Char(
        string="Indique cual"
    )
    equipment_assign_to = fields.Selection(
        [
            ('department', 'Department'),
            ('employee', 'Employee'),
            ('other', 'Other'),
            ('without_using', 'Without using'),
        ],
        string='Used By',
        required=True,
        default='without_using'
    )
    type_assignment = fields.Selection(
        [
            ('intial', 'Asignación Inicial'),
            ('replacement', 'Remplazo o Actualización'),
            ('culminaction', 'Termino de Relación Laboral')
        ],
        string="Tipo de Asignación",
        # required=True,
        help="Denife el tipo se Asignación de Equipos"
    )

    @api.depends('equipment_assign_to')
    def _compute_equipment_assign(self):
        for equipment in self:
            if equipment.equipment_assign_to == 'employee':
                equipment.department_id = False
                equipment.employee_id = equipment.employee_id
                equipment.assign_date = fields.Date.context_today(self)
            elif equipment.equipment_assign_to == 'department':
                equipment.employee_id = False
                equipment.department_id = equipment.department_id
                equipment.assign_date = fields.Date.context_today(self)
            elif equipment.equipment_assign_to == 'without_using':
                equipment.employee_id = False
                equipment.department_id = False
                equipment.assign_date = False
            else:
                equipment.department_id = equipment.department_id
                equipment.employee_id = equipment.employee_id
                equipment.assign_date = fields.Date.context_today(self)


