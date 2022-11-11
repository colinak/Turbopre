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

class ToolRoomCategory(models.Model):
    _inherit = 'product.category'
    # _description = 'Toolroom Category'
    # _order = 'name'
    # _rec_name = 'name'


    # parent_id = fields.Many2one(
        # 'toolroom.category',
        # string="Categoría Padre",
        # help="Categoría Padre"
    # )
    dpto_responsible_id = fields.Many2one(
        'hr.department',
        string="Responsible Department",
        help="Responsible Department"
    )
    technician_user_id = fields.Many2one(
        'res.users',
        string="Responsible",
        help="Responsible"
    )
    note = fields.Text(string="Notes")



