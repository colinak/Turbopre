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


class ResPartner(models.Model):
    _inherit = 'res.partner'


    
    customer = fields.Boolean(
        string='Is a Customer', 
        default=False,
        help="Check this box if this contact is a customer. It can be selected in sales orders."
    )
    supplier = fields.Boolean(
        string='Is a Vendor',
        default=False,
       help="Check this box if this contact is a vendor. It can be selected in purchase orders."
    )
    employee = fields.Boolean(
        string="Is a Employee", 
        default=False,
        help="Check this box if this contact is an Employee."
    )

