#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class QualityEquipment(models.Model):
    _name = 'quality.equitment'
    _description = 'Quiality Equipment'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="Name")
    category_id = fields.Many2one(
        'quality.equitment.category',
        string="Category",
        help="Category Equipment"
    )
    code = fields.Char(string="Code")
    image_1920 = fields.Image(
        string="Image",
    )
    make_id = fields.Many2one(
        'quality.equitment.manufacturers',
        string="Make",
        help="Make"
    )
    model = fields.Char(string="Model")
    serial_no = fields.Char(string="Serial N°")
    rango = fields.Char(string="Range")
    appreciation = fields.Char(string="Appreciation")
    frequency_cal_ver = fields.Integer(string="Calibration Frequency")
    clasification = fields.Selection(
        [('F', 'Follow-up'), ('m', 'Measurement')],
        string="Clasification"
    )
    status = fields.Char(string="Status")
    stage = fields.Char(string="Stage")
    calibration_date = fields.Date(string="Calibration Date")
    expiration_date = fields.Date(string="Expiration Date")
    location = fields.Char(string="Location")
    shelf_number = fields.Char(string="Shelf Number")
    shelf_position = fields.Char(string="Shelf Position")
    technician_user_id = fields.Many2one(
        "res.users",
        string="Responsible"
    )
    out_of_service = fields.Boolean(string="Ouf of Service")
    active = fields.Boolean(string="Active", default=True)



