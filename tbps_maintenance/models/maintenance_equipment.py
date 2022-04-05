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
    _order = 'name'


    def default_current_user_id(self):
        user_id = self.env.user.id
        user = self.env['hr.employee'].search(
            [('user_id.id', '=', user_id)]
        )
        return user


    brand_id = fields.Many2one(
        'maintenance.manufacturers',
        string="Make",
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
            ('in_custody', 'In Custody'),
            ('discarded', 'Out of service'),
        ],
        string="Stage",
        default="available",
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
            ('culmination', 'Termino de Relación Laboral')
        ],
        string="Tipo de Asignación",
        help="Define el tipo se Asignación de Equipos"
    )
    type_discard = fields.Selection(
        selection=[
            ('discard', 'Discard'), 
            ('replacement', 'Replacement'),
            ('donation', 'Donation')
        ],
        string="Tipo de Desecho",
        help="Define si el equipo sirve para respuesto, o debe ser desechado"
    )
    out_of_service = fields.Boolean(
        string="Out of Service",
        default=False
    )
    image_1920 = fields.Image(
        string="Image",
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
    

    @api.onchange('equipment_assign_to')
    def _onchange_equipment_assign_to(self):
        if self.equipment_assign_to == 'unassigned' and self.stage != 'discarded':
            self.type_assignment = False
        elif self.equipment_assign_to != 'unassigned':
            self.out_of_service = False
            self.type_discard = False


    @api.onchange('out_of_service')
    def _onchange_out_of_service(self):
        if self.out_of_service == False:
            self.type_discard = False


    @api.depends('stage')
    def reserve(self):
        if self.stage == 'assigned':
            self.stage = 'in_custody'

    @api.depends('stage')
    def set_free(self):
        if self.stage == 'in_custody':
            self.stage = 'assigned'

    @api.depends('stage')
    def unassigned(self):
        if self.stage == 'in_custody' or self.stage == 'assigned':
            self.equipment_assign_to = 'unassigned'
            self.type_assignment = False
        else:
            raise UserError('Error, Contacte al Administrador del Sistema.')


    @api.depends('stage')
    def refurbish(self):
        if self.stage == 'out_of_service' or self.active == False:
            self.stage = 'available'
            self.out_of_service = False
            self.active = True


    @api.model
    def create(self, vals):
        res = super(MaintenanceEquipment, self).create(vals)
        if res.equipment_assign_to == 'unassigned' and not res.out_of_service:
            res.stage = 'available'
        elif res.equipment_assign_to != 'unassigned':
            res.stage = 'assigned'
        else: 
            if res.out_of_service:
                if res.type_discard == 'discard':
                    res.location = "Archivo Muerto"
                res.stage = 'discarded'
                res.active = False
        return res



    def write(self, vals):
        if vals.get('out_of_service'):
            if vals.get('type_discard') == 'discard':
                self.location = "Archivo Muerto"
            self.stage = 'discarded'
            self.active = False
        elif vals.get('out_of_service') == False:
            self.active = True
            self.location = False
            self.stage = 'available'
            self.type_discard = False
        else:
            if vals.get('equipment_assign_to') == 'unassigned' and not vals.get('out_of_service'):
                self.stage = 'available'
                self.location = False
                self.type_discard = False
                self.active = True
            elif (vals.get('equipment_assign_to') == 'employee' or
                    vals.get('equipment_assign_to') == 'department' or
                    vals.get('equipment_assign_to') == 'other'):
                self.stage = 'assigned'

        res = super(MaintenanceEquipment, self).write(vals)

        return res


