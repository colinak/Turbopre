#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

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

