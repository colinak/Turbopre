#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
#
# Author: KEWITZ COLINA
# Copyleft: 2020-Present.
# License LGPL-3.0 or later (http: //www.gnu.org/licenses/lgpl.html).
#
###############################################################################

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class TrStockManufacturers(models.Model):
    _name = 'tr.stock.manufacturers'
    _description = 'Fabricantes'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="Marca", required=True)
    image = fields.Image(string="Logo", max_width=128, max_height=128)
    sequence = fields.Integer(string="Secuencia")
    note = fields.Text(string="Notas")
