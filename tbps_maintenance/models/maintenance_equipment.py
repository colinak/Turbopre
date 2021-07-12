#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'
    _description = 'Equipment'



    def default_current_user_id(self):
        user_id = self.env.user.id
        user = self.env['hr.employee'].search(
            [('user_id.id', '=', user_id)]
        )

        return user


    brand_id = fields.Many2one(
        'maintenance.manufacturers',
        string="Make",
        # required=True,
        help="Make Equipment"
    )
    depto_responsible_id = fields.Many2one(
        'hr.department',
        string="Depto Responsible",
        required=True,
        help="Department Responsible for Equipment"
    )
    stage = fields.Selection(
        [
            ('available', 'Available'),
            ('assigned', 'Assigned'),
            ('discarded', 'Out of service'),
        ],
        string="Stage",
        default="available",
        # compute=_compute_stage,
        # store=True,
        help="Stage"
    )
    other = fields.Char(
        string="Indique cual"
    )
    equipment_assign_to = fields.Selection(
        [
            ('department', 'Department'),
            ('employee', 'Employee'),
            ('other', 'Other'),
            ('unassigned', 'Unassigned'),
        ],
        string='Used By',
        required=True,
        default='unassigned'
    )
    type_assignment = fields.Selection(
        [
            ('initial', 'Asignación Inicial'),
            ('replacement', 'Remplazo o Actualización'),
            ('culminaction', 'Termino de Relación Laboral')
        ],
        string="Tipo de Asignación",
        help="Denife el tipo se Asignación de Equipos"
    )

    @api.depends('equipment_assign_to')
    def _compute_equipment_assign(self):
        for equipment in self:
            if equipment.equipment_assign_to == 'employee':
                equipment.department_id = False
                equipment.other = ""
                equipment.employee_id = equipment.employee_id
                equipment.assign_date = fields.Date.context_today(self)
            elif equipment.equipment_assign_to == 'department':
                equipment.employee_id = False
                equipment.other = ""
                equipment.department_id = equipment.department_id
                equipment.assign_date = fields.Date.context_today(self)
            elif equipment.equipment_assign_to == 'unassigned':
                equipment.employee_id = False
                equipment.department_id = False
                equipment.assign_date = False
                equipment.other = ""
                equipment.assign_date = fields.Date.context_today(self)
            else:
                equipment.employee_id = False
                equipment.department_id = False
                equipment.other = equipment.other
                equipment.assign_date = fields.Date.context_today(self)


    @api.model
    def create(self, vals):
        _logger.info(">>>>>>>>>>>>>>CREATE<<<<<<<<<<<<<<")
        res = super(MaintenanceEquipment, self).create(vals)
        if res.equipment_assign_to == 'unassigned':
            res.stage = 'available'
        elif res.equipment_assign_to != 'unassigned':
            res.stage = 'assigned'
            # res.type_assignment = 'initial'
        return res



    def write(self, vals):
        _logger.info(">>>>>>>>>>>>>>WRITE<<<<<<<<<<<<<<")
        if vals.get('equipment_assign_to') == 'unassigned':
            vals['stage'] = 'available'
        elif vals.get('equipment_assign_to') != 'unassigned':
            vals['stage'] = 'assigned'

        # _logger.info("Usado por: " + self.equipment_assign_to)
        # if self.equipment_assign_to != 'unassigned':
            # equipment_assign_to = self.equipment_assign_to
            # if vals.get('equipment_assign_to') == 'unassigned':
                # raise UserError('Este Equipos Esta asignado a un empleado, debe recibir el equipo antes de poder modificarlo.')
            # elif vals.get('equipment_assign_to') != 'unassigned' and vals.get('equipment_assign_to') != equipment_assign_to:
                # raise UserError('No Puede Modificar un Equipo de esta Forma debe Remplazar el Equipo desde el boton Remplazar.')

        # elif self.equipment_assign_to == 'unassigned':
            # equipment_assign = self.equipment_assign_to
            # if (vals.get('equipment_assign_to') == 'employee' or 
                    # vals.get('equipment_assign_to') == 'department' or 
                    # vals.get('equipment_assign_to') == 'other'):
                # _logger.info(">>>>>>>>>>>>>>IF<<<<<<<<<<<<<<")
                # _logger.info("Vals: " + str(vals))
                # vals['stage'] = 'assigned'
                # if self.type_assignment == False:
                    # vals['type_assignment'] = 'initial'
                    # _logger.info("Vals 2: " + str(vals))
                # elif self.type_assignment == 'initial':
                    # vals['type_assignment'] = 'replacement'

            # raise UserError('Equipo sin Asignar')

        res = super(MaintenanceEquipment, self).write(vals)

        return res


