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
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class QualityLocation(models.Model):
    _name = 'quality.location'
    _description = 'Ubicaciones'
    _rec_name = 'complete_name'
    _order = 'name'

    name = fields.Char(
        string="Name"
    )
    complete_name = fields.Char(
        string="Complete Name"
    )
