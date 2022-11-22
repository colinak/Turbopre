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

class HrEmployeeBase(models.Model):
    _inherit = 'hr.employee.base'


    equipment_id = fields.One2many(
        "",
        "employee_id",
        string="Equipos/Herramientas"
    )
    



