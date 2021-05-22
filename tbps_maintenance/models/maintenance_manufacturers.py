#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class ProductBrand(models.Model):
    _name = 'maintenance.manufacturers'
    _description = 'Manufacturers'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string="Make", required=True)
    image = fields.Image(string="Logo", max_width=128, max_height=128)

