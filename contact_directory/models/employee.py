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


class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    is_operations = fields.Boolean(
        string="It's Operations",
        # default=True,
        held="Indica si el usuario podra prestar herramientas."
    )
    barcode = fields.Char(groups="hr.group_hr_user,base.group_user")
    pin = fields.Char(groups="hr.group_hr_user,base.group_user")

class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'


    is_operations = fields.Boolean(
        string="It's Operations",
        # default=True,
        held="Indica si el usuario podra prestar herramientas."
    )
