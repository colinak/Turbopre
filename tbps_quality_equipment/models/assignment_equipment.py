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
import logging
_logger = logging.getLogger(__name__)


class QualityStatus(models.Model):
    _name = 'assignment.equipment'
    _description = 'Assignment Equipment'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(string="Description")
    project = fields.Char(string="Project")
    services_order = fields.Char(string="Services Order")
    location = fields.Char(string="Location")
    equipment_id = fields.One2many(
        'quality.equipment',
        'assigned_id',
        string="Equipments"
    )
