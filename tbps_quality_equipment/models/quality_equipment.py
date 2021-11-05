#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)


class QualityEquipment(models.Model):
    _name = 'quality.equitment'
    _description = 'Quiality Equipment'
    _order = 'name'
    _rec_name = 'name'



    name = fields.Char(
        string="Name",
        # required=True,
        help="Equipment Description"
    )
    equipment_id = fields.Many2one(
        'quality.equitment.category',
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
        'quality.equitment.manufacturers',
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
        'quality.equitment.clasification',
        string="Clasification"
    )
    status_id = fields.Many2one(
        'quality.status',
        string="Status",
        required=True,
        help="Calibration Status"
    )
    stage = fields.Char(string="Stage")
    calibration_date = fields.Date(string="Calibration Date")
    expiration_date = fields.Date(string="Expiration Date")
    location = fields.Char(string="Location", required=True)
    shelf_number = fields.Char(string="Shelf Number")
    shelf_position = fields.Char(string="Shelf Position")
    technician_user_id = fields.Many2one(
        "res.users",
        string="Responsible",
        required=True
    )
    out_of_service = fields.Boolean(
        string="Ouf of Service",
        # compute='_compute_out_of_service',
        # store=False
    )
    active = fields.Boolean(string="Active", default=True)


    @api.constrains('make_id', 'category_id')
    def _check_code_unique(self):
        if self.make_id and self.category_id:
            pass



    @api.onchange('frequency_cal_ver', 'calibration_date')
    def _onchange_expiration_date(self):
        # if self.frequency_cal_ver != 0 and self.calibration_date:
        _logger.info("Frecuencia: " + str(self.frequency_cal_ver))
        if self.frequency_cal_ver != 0 and self.calibration_date:
            self.expiration_date = fields.Date.context_today(self)






