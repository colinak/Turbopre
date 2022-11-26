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

class ToolRoomAttribute(models.Model):
    _inherit = 'product.attribute'
    # _description = 'Toolroom Attribute'
    # _order = 'name'
    # _rec_name = 'name'
