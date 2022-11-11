#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################################################
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
# import os


class CheckAvailabilityToolWizard(models.TransientModel):
    _name = 'check.availability.tool.wizard'
    _description = 'Check Availability Tool'

    name = fields.Char(
        string="Nombre",
        required=True,
        help="Ingrese el nombre de la herramienta que desea consultar"
    )
    quantity = fields.Integer(
        string="Cantidad"
    )
