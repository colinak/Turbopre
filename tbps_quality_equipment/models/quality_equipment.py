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
        'quality.category',
        string="Category",
        help="Category Equipment"
    )
    code = fields.Char(string="Code")
    image_1920 = fields.Image(
        string="Image",
    )
    make_id = fields.Many2one(
        'quiality.manufacturers',
        string="Make",
        help="Make"
    )
    model = fields.Char(string="Model")
    serial_no = fields.Char(string="Serial N°")
    rango = fields.Char(string="Range")
    appreciation = fields.Char(string="Appreciation")
    frequency_cal_ver = fields.Char(string="Calibration Frequency")
    clasification = fields.Selection(
        [('F', 'Follow-up'), ('m', 'Measurement')],
        string="Clasification"
    )
    location = fields.Char(string="Location")
    # ouf_of_service = fields.Boolean(string="Ouf of Service")
    # active = fields.Boolean(string="Active", default=True)



