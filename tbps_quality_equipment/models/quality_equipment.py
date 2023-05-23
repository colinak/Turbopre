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
    image_1920 = fields.Image(
        string="Image",
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
        help="Measurement value range"
    )
    appreciation = fields.Char(
        string="Appreciation",
        help="Minimum unit of measure"
    )
    frequency_cal_ver = fields.Integer(
        string="Calibration Frequency",
        help="Calibration or verification frequency"
    )
    clasification_id = fields.Many2one(
        'quality.equipment.clasification',
        string="Clasification"
    )
    status_id = fields.Many2one(
        'quality.status',
        string="Status",
        # compute="_compute_calibration_frequency",
        store=True,
        help="Calibration Status"
    )
    # status = fields.Selection(
        # [
            # ('available', 'Available'),
            # ('assigned', 'Assigned'),
            # ('loan', 'Loan'),
            # ('in_custody', 'In Custody'),
            # ('discarded', 'Out of Service'),
        # ],
        # string="Stage",
        # default='available'
    # )
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
#         compute="_compute_calibration_frequency",
    )
    expiration_date = fields.Date(
        string="Expiration Date",
        # compute="_compute_calibration_frequency",
    )
    location = fields.Char(string="Location", required=True)
    shelf_number = fields.Char(string="Shelf Number")
    shelf_position = fields.Char(string="Shelf Position")
    technician_user_id = fields.Many2one(
        "res.users",
        string="Responsible",
        required=True
    )
    assigned_id = fields.Many2one(
        'assignment.equipment',
        string="Assigned"
    )
    calibration_verification_ids = fields.One2many(
        'quality.traceability.equipment',
        'equipment_id',
        string="Calibrations Verification"
    )
    note = fields.Text(string="Notes", help="Observations")
    out_of_service = fields.Boolean(
        string="Ouf of Service",
        # compute='_compute_out_of_service',
        # store=False
    )
    active = fields.Boolean(string="Active", default=True)

    _sql_constraints = [
        ('name_serial_no', 'UNIQUE(serial_no)', 'There is another asset with this serial number!'),
        ('code_unique', 'UNIQUE(code)', 'There is another asset with this code!')
    ]


    @api.constrains('make_id')
    def _check_code_unique(self):
        if self.make_id:
            pass


    @api.onchange('status_id')
    def _onchange_status(self):
        if self.status_id.name == "No Requiere Calibracion" or self.status_id.id == 5:
            self.frequency_cal_ver = 0
            self.calibration_date = ""
            self.expiration_date = ""


    # @api.depends('calibration_verification_ids')
    # def _compute_calibration_frequency(self):
        # _logger.info("###############################################")
        # _logger.info("SELF: " + str(self.calibration_verification_ids))
        # _logger.info("IDS: " + str(self.calibration_verification_ids[-1]))
        # if self.calibration_verification_ids:
            # _logger.info("SELF: " + str(self.calibration_verification_ids))
            # for rec in self:
                # _logger.info("REC: "+ str(rec))
                # cal_verif = rec.calibration_verification_ids[-1]
                # rec.calibration_date = cal_verif.date_execute
                # rec.expiration_date = cal_verif.date_expiration
                # rec.status_id = cal_verif.final_condition_id
        # else:
            # pass




