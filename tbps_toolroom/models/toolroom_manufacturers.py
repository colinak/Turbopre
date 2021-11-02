#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class ToolRoomManufacturers(models.Model):
    _name = 'toolroom.manufacturers'
    _description = 'Toolroom Manufacturers'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="Name", required=True)
    image = fields.Binary(string="Image", max_width=128, max_height=128)
    note = fields.Text(string="Notes")

