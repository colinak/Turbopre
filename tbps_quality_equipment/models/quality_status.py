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
    _name = 'quality.status'
    _description = 'Quiality Status'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Name",
        required=True,
        help="Description"
    )
    active = fields.Boolean(string="Archived", default=True)

