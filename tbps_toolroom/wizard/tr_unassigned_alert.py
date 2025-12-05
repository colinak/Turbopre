#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################################################
#
# Author: KEWITZ COLINA
# Copyleft: 2020-Present.
# License LGPL-3.0 or later (http: //www.gnu.org/licenses/lgpl.html).
#
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)
# import os


class TrUnassignedAlert(models.TransientModel):
    _name = 'tr.unassigned.alert.wizard'
    _description = 'Unassigned Alert'

    msg = fields.Char(
        string="Msg",
    )

