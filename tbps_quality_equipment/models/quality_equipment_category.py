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


class QualityEquipmentCategory(models.Model):
    _name = 'quality.equipment.category'
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
        'tps.employee',
        string="Responsible",
        help="Responsible"
    )
    note = fields.Text(string="Notes")
    equipment_ids = fields.One2many(
        "quality.equipment",
        "equipment_id",
        string="Equipos",
        help="Listado de Equipos"
    )
    equipment_count = fields.Integer(
        string="Equipos",
        compute="_compute_equipment_count"
    )
    active = fields.Boolean(
        string="Activo?",
        default=True
    )



    @api.depends('equipment_ids')
    def _compute_equipment_count(self):
        for category in self:
            category.equipment_count = len(category.equipment_ids)
