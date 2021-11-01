#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class QualityEquipmentCategory(models.Model):
    _name = 'quality.equitment.category'
    _description = 'Quiality Equipment Category'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="Name", required=True)
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

