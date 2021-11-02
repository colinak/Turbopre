#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class ToolRoomEquipment(models.Model):
    _name = 'toolroom.equipment'
    _description = 'Toolroom Equipment'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="Name", required=True)
    image = fields.Binary(string="Image", max_width=128, max_height=128)
    category_id = fields.Many2one(
        'toolroom.category',
        string="Category",
        help="Category of tools"
    )
    make_id = fields.Many2one(
        'toolroom.manufacturers',
        string="Make",
        help="Manufacturers of tools"
    )
    model = fields.Char(string="Model")
    measure = fields.Char(string="Measure")
    quadrant = fields.Char(string="Quadrant")
    identification_code = fields.Char(string="Identification Code")
    uom_id = fields.Many2one(
        'uom.uom',
        string="Units of Measure"
    )
    location = fields.Char(string="Location")
    serial_number = fields.Char(string="Serial Number")
    # status = fields.Selection()
    # stage = fields.Selection()
    active = fields.Boolean(string="Active", default=True)
    out_of_service = fields.Boolean(string="Out of Service", default=False)

