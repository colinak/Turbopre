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


class QualityEquipmentClasification(models.Model):
    _name = 'quality.equipment.clasification'
    _description = 'Quiality Equipment Clasification'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="Name", required=True)
    image = fields.Binary(string="Image", max_width=128, max_height=128)
    note = fields.Text(string="Notes")
    active = fields.Boolean(string="Archived", default=True)
