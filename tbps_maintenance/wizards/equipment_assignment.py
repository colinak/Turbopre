#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class EquipmanetAssignment(models.TransientModel):
    _name = 'equipment.assignment.report.wizar'
    _description = 'Asignación de Equipos'



    def default_current_user_id(self):
        user_id = self.env.user.id
        user = self.env['hr.employee'].search(
            [('user_id.id', '=', user_id)]
        )
        return user


    name = fields.Char(
        string="Name",
        compute="_compute_name"
    )
    equipment_assignment_to = fields.Selection(
        [
            ('department', 'Department'),
            ('employee', 'Employee'),
            ('project', 'Proyecto')
        ],
        string="Used By",
        required=True,
        default='employee'
    )
    department_id = fields.Many2one(
        'hr.department',
        string="Department"
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string="Employee"
    )
    project_id = fields.Many2one(
        'maintenance.location',
        string="Proyecto",
        domain="[('type_location', '=', 'external')]"
    )
    date_assign = fields.Date(
        string="Assigned Date",
        default=fields.Date.today(),
        readonly=False
    )
    equipment_ids = fields.Many2many(
        'maintenance.equipment',
        string="Equipments",
    )
    note = fields.Text(
        string="Observations"
    )
    type_report = fields.Selection([
            ('assignment', 'Assignment'),
            ('reception','Reception')
        ],
        string="Type Report"
    )
    location = fields.Char(strinG="Location")
    location_id = fields.Many2one(
        "maintenance.location",
        string="Ubicación",
    )


    @api.depends('department_id', 'employee_id', 'project_id')
    def _compute_name(self):
        if self.equipment_assignment_to == 'department':
            self.name = self.department_id.name
        elif self.equipment_assignment_to == 'employee':
            self.name = self.employee_id.name
        elif self.equipment_assignment_to == 'project':
            self.name = self.project_id.complete_name


    @api.onchange('equipment_assignment_to')
    def _onchange_equipment_assignment_to(self):
        if self.equipment_assignment_to != 'department':
            self.department_id = ''
            self.project_id = False
            self.equipment_ids = [(6, 0, [])]
        elif self.equipment_assignment_to != 'employee':
            self.employee_id = ''
            self.project_id = False
            self.equipment_ids = [(6, 0, [])]
        elif self.equipment_assignment_to != 'project':
            self.employee_id = ''
            self.department_id = ''
            self.equipment_ids = [(6, 0, [])]

    @api.onchange('department_id')
    def _onchange_department(self):
        if self.department_id != False:
            self.equipment_ids = [(6, 0, [])]

    @api.onchange('employee_id')
    def _onchange_employee(self):
        if self.employee_id != False:
            self.equipment_ids = [(6, 0, [])]

    @api.onchange('project_id')
    def _onchange_project(self):
        if self.project_id != False:
            self.equipment_ids = [(6, 0, [])]

    def get_report(self):
        if len(self.equipment_ids) > 0:
            try:
                return self.env.ref(
                    'tbps_maintenance.action_equipment_assignment_report'
                ).report_action(self)
                # ,self.next_func_toclose()
            except:
                raise UserError(
                    "Disculple Hubo un Error al Intenter Imprimir el Reporte" + 
                    "Intentelo de Nuevo, y si el Problema persiste, " +
                    "Contacte a su Proveedor de Servicios."
                )
            
        else:
            raise UserError(
                "Seleccione al menos un Registro para Generar el Reporte"
            )


