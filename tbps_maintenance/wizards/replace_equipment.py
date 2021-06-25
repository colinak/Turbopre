#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class ReplaceEquipment(models.TransientModel):
    _name = 'replace.equipment.wizard'
    _description = 'Replace Equipment'


    def _default_equipment_name(self):
        return self.env['maintenance.equipment'].browse(
            self._context.get('active_id')
        )


    @api.depends('equipment_name')
    def _compute_data(self):
        if self.equipment_name:
            self.make = self.equipment_name.brand_id.name
            self.model = self.equipment_name.model
            self.no_serial = self.equipment_name.serial_no


    equipment_id = fields.Many2one(
        'maintenance.equipment',
        strinf="Equipment",
        domain="[('stage', '=', 'available')]",
        required=True,
        help="New equipment to assigned"
    )
    equipment_name = fields.Many2one(
        'maintenance.equipment',
        string="Equipment to Replace",
        default=_default_equipment_name
    )
    make = fields.Char(
        string="Make",
        compute=_compute_data
    )
    check_make = fields.Boolean(
        string="Check Make",
        default=False
    )
    model = fields.Char(
        string="Model",
        compute=_compute_data
    )
    check_model = fields.Boolean(
        string="Check model",
        default=False
    )
    no_serial = fields.Char(
        string="N° Serial",
        compute=_compute_data
    )
    check_serial = fields.Boolean(
        string="Check Serial",
        default=False
    )
    observations = fields.Text(
        string="Observations"
    )


    def confirm_replace_equipment(self):
        _logger.info('>>>>>>>>>>>>>>>>>>>CONFIRM<<<<<<<<<<<<<<<<<<<')
        if self.equipment_id and self.check_make and self.check_model and self.check_serial:
            _logger.info('>>>>>>>>>>>>>>>>>>>IF<<<<<<<<<<<<<<<<<<<')
            if self.equipment_name.equipment_assign_to == 'employee':
                _logger.info('>>>>>>>>>>>>>>>>>>>1<<<<<<<<<<<<<<<<<<<')
                self.equipment_id.write({
                    'equipment_assign_to': 'employee',
                    'stage': 'assigned',
                    'employee_id': self.equipment_name.employee_id.id,
                    'type_assignment': 'replacement',
                    'assign_date': fields.Date.context_today(self),
                    'location': self.equipment_name.location,
                })
                _logger.info('>>>>>>>>>>>>>>>>>>>A1<<<<<<<<<<<<<<<<<<<')
            elif self.equipment_name.equipment_assign_to == 'department':
                _logger.info('>>>>>>>>>>>>>>>>>>>2<<<<<<<<<<<<<<<<<<<')
                self.equipment_id.write({
                    'equipment_assign_to': 'department',
                    'stage': 'assigned',
                    'employee_id': self.equipment_name.department_id.id,
                    'type_assignment': 'replacement',
                    'assign_date': fields.Date.context_today(self),
                    'location': self.equipment_name.location,
                })
            elif self.equipment_name.equipment_assign_to == 'other':
                _logger.info('>>>>>>>>>>>>>>>>>>>3<<<<<<<<<<<<<<<<<<<')
                self.equipment_id.write({
                    'equipment_assign_to': 'other',
                    'stage': 'assigned',
                    'employee_id': self.equipment_name.other,
                    'type_assignment': 'replacement',
                    'assign_date': fields.Date.context_today(self),
                    'location': self.equipment_name.location,
                })
            else:
                _logger.info('>>>>>>>>>>>>>>>>>>>4<<<<<<<<<<<<<<<<<<<')
                raise UserError("""
                    Unable to replace equipment if data does not match.! \n
                    Consult with the Administrator of the Sitema.!
                """)
            self.equipment_name.write({
                'equipment_assign_to': 'unassigned',
                'stage': 'available',
                'employee_id': False,
                'type_assignment': False,
                'assign_date': fields.Date.context_today(self),
                'location': False
            })
        else:
            raise UserError('You must select the new team to assign.!')




