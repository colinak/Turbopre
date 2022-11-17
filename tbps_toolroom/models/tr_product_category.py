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
    _name = 'tr.product.category'
    _description = 'Toolroom Product Category'
    _order = 'complete_name'
    _rec_name = 'complete_name'


    name = fields.Char(
        string="Nombre",
        required=True,
        help=""
    )
    complete_name = fields.Char(
        string="Nombre completo",
        required=True,
        help=""
    )
    parent_id = fields.Many2one(
        'tr.product.category',
        string="Categoría Padre",
        help="Categoría Padre"
    )
    child_ids = fields.One2many(
        'tr.product.category',
        'parent_id',
        string="Categorías hijas",
        help="Categorías hijas"
    )
    product_count = fields.Integer(
        string="Cantidad de productos"
    )

    note = fields.Text(string="Notas")



