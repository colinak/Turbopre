#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    make_id = fields.Many2one(
        'toolroom.manufacturers',
        string="Make",
        help="Manufacturers of tools"
    )
    model = fields.Char(string="Model")
    measure_id = fields.Many2one(
        'toolroom.measure',
        string="Measure"
    )
    quadrant_id = fields.Many2one(
        'toolroom.quadrant',
        string="Quadrant"
    )
    identification_code = fields.Char(string="Identification Code")
    uom_id = fields.Many2one(
        'uom.uom',
        string="Units of Measure"
    )
    location = fields.Char(string="Location")
    # serial_number = fields.Char(string="Serial Number")
    # active = fields.Boolean(string="Active", default=True)
    # out_of_service = fields.Boolean(string="Out of Service", default=False)


