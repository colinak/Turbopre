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
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class QualityEquipment(models.Model):
    _name = 'quality.equipment'
    _description = 'Quiality Equipment'
    _order = 'name'
    _rec_name = 'equipment_id'


    @api.onchange('equipment_id')
    def _onchange_equipment(self):
        if self.equipment_id:
            self.name = ""
            self.name = self.equipment_id.name

    name = fields.Char(
        string="Name",
        # required=True,
        help="Equipment Description"
    )
    equipment_id = fields.Many2one(
        'quality.equipment.category',
        string="Equipment",
        required=True,
        help="Category Equipment"
    )
    code = fields.Char(
        string="Code",
        required=True,
        help="Code for Equipment"
    )
    make_id = fields.Many2one(
        'quality.equipment.manufacturers',
        string="Make",
        help="Make for Equipment"
    )
    model = fields.Char(string="Model")
    serial_no = fields.Char(string="Serial N°")
    rango = fields.Char(
        string="Range",
        required=True,
        help="Measurement value range"
    )
    appreciation = fields.Char(
        string="Appreciation",
        required=True,
        help="Minimum unit of measure"
    )
    frequency_cal_ver = fields.Integer(
        string="Calibration Frequency",
        help="Calibration or verification frequency"
    )
    cali_ver_string = fields.Char(
        string="Frecuencia Calibración",
        compute="_compute_cali_ver_string"
    )
    clasification_id = fields.Many2one(
        'quality.equipment.clasification',
        string="Clasification"
    )
    status_id = fields.Many2one(
        'quality.status',
        string="Status",
        default=lambda self: self.env['quality.status'].search(
            [('id', '=', 1)],limit=1),
        help="Calibration Status"
    )
    stage = fields.Selection(
        [
            ('available', 'Available'),
            ('assigned', 'Assigned'),
            ('loan', 'Loan'),
            ('in_custody', 'In Custody'),
            ('discarded', 'Out of Service'),
        ],
        string="Stage",
        default='available'
    )
    calibration_date = fields.Date(
        string="Calibration Date",
    )
    expiration_date = fields.Date(
        string="Expiration Date",
    )
    location_id = fields.Many2one(
        "quality.location",
        string="Location", 
        required=True,
        help="Seleccione la ubicación del equipo."
    )
    shelf_number = fields.Char(string="Shelf Number")
    shelf_position = fields.Char(string="Shelf Position")
    technician_user_id = fields.Many2one(
        "hr.employee",
        string="Responsible",
        required=True
    )
    employee_assigned_id = fields.Many2one(
        "hr.employee",
        string="Empleado Asignado",
    )
    # assigned_id = fields.Many2one(
        # 'assignment.equipment',
        # string="Assigned"
    # )
    calibration_verification_ids = fields.One2many(
        'quality.traceability.equipment',
        'equipment_id',
        string="Calibrations Verification"
    )
    note = fields.Text(string="Notes", help="Observations")
    out_of_service = fields.Boolean(
        string="Ouf of Service",
    )
    active = fields.Boolean(string="Active", default=True)

    # all image fields are base64 encoded and PIL-supporte
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)

    # resized fields stored (as attachment) for performance
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)

    _sql_constraints = [
        ('name_serial_no', 'UNIQUE(serial_no)', 'There is another asset with this serial number!'),
        ('code_unique', 'UNIQUE(code)', 'There is another asset with this code!')
    ]


    @api.constrains('make_id')
    def _check_code_unique(self):
        if self.make_id:
            pass

    def _compute_cali_ver_string(self):
        for rec in self:
            if rec.frequency_cal_ver > 0:
                rec.cali_ver_string = f"{rec.frequency_cal_ver} Meses"
            else:
                rec.cali_ver_string = "N/A"


    @api.onchange('status_id')
    def _onchange_status(self):
        if self.status_id.name == "No Requiere Calibracion" or self.status_id.id == 5:
            self.frequency_cal_ver = 0
            self.calibration_date = ""
            self.expiration_date = ""


    @api.onchange('calibration_date', 'frequency_cal_ver')
    def _onchange_calibration_frequency(self):
        if self.calibration_date and self.frequency_cal_ver != 0:
            expired_date = (
                fields.Datetime.from_string(self.calibration_date) + 
                relativedelta(months=int(self.frequency_cal_ver))
            )
            self.expiration_date = expired_date


    @api.onchange('equipment_id')
    def _onchange_equipment(self):
        if self.equipment_id:
            self.technician_user_id = self.equipment_id.technician_user_id.id


    def write(self, vals):
        if vals.get('calibration_verification_ids'):
            _logger.info("Datos: " + str(vals.get('calibration_verification_ids')))
            for rec in vals.get('calibration_verification_ids'):
                if rec[0] == 0:
                    self.status_id = rec[2].get('final_condition_id')
                    self.calibration_date = rec[2].get('date_execute')
                    self.expiration_date = rec[2].get('date_expiration')
                     
        res = super(QualityEquipment, self).write(vals)
        return res



