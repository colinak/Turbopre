#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class TrStockPicking(models.Model):
    _inherit = 'stock.picking'
    _name = 'tr.stock.picking'
    _description = 'Toolroom Operaciones'
    _order = 'name'
    _rec_name = 'name'

