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


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'


    tools_ids = fields.One2many(
        "product.product",
        "employee_id",
        string="Equipos/Herramientas",
    )



# class HrEmployeePrivate(models.Model):
    # _inherit = 'hr.employee'


    # tools_ids = fields.One2many(
        # "product.product",
        # "employee_id",
        # string="Equipos/Herramientas"
    # )
    


