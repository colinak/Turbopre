#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class ToolRoomEquipment(models.Model):
    _name = 'toolroom.equipment'
    _description = 'Toolroom Equipment'
    _order = 'name'
    _rec_name = 'name'


    # @api.depends('category_id', 'make_id', 'model', 'measure_id', 'quadrant_id')
    # def _compute_name(self):
        # _logger.info("########################################3")
        # self.name = self.category_id.name + ' ' + self.measure_id.name + ' ' + self.quadrant_id.name
        # if self.category_id and self.model and self.make_id:
            # for record in self:
                # record.name = record.category_id.name + record.measure_id.name + \
                # " " + record.quadrant_id.name + " " + record.make_id.name + \
                # " " + record.model
            # self.name
            # _logger.info("Nombre: " + str(self.name))
            

    name = fields.Char(
        string="Name",
        # compute=_compute_name
    )
    image = fields.Binary(string="Image", max_width=128, max_height=128)
    category_id = fields.Many2one(
        'toolroom.category',
        string="Category",
        help="Category of tools"
    )
    make_id = fields.Many2one(
        'toolroom.manufacturers',
        string="Make",
        help="Manufacturers of tools"
    )
    model = fields.Char(string="Model")
    measure_id = fields.Many2one(
        'toolroom.measure',
        string="Measure"
    )
    quadrant_id = fields.Many2one(
        'toolroom.quadrant',
        string="Quadrant"
    )
    identification_code = fields.Char(string="Identification Code")
    uom_id = fields.Many2one(
        'uom.uom',
        string="Units of Measure"
    )
    location = fields.Char(string="Location")
    serial_number = fields.Char(string="Serial Number")
    active = fields.Boolean(string="Active", default=True)
    out_of_service = fields.Boolean(string="Out of Service", default=False)

