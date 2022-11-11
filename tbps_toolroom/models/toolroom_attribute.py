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


    # value_ids = fields.One2many(
        # 'toolroom.attribute.value',
        # 'attribute_id',
        # string="Valores",
        # help="Valores para el atributo"
    # )
    # attribute_line_ids = fields.One2many(
        # 'toolroom.attribute.value',
        # 'attribute_id',
        # string="Líneas",
    # )
# product_attribute_value_product_template_attribute_line_rel



# class ToolRoomAttributeValue(models.Model):
    # _name = 'toolroom.attribute.value'
    # _inherit = 'product.attribute.value'
    # _description = 'Toolroom Attribute Value'
    # _order = 'name'
    # _rec_name = 'name'



    # toolroom_attribute_value_id = fields.Many2one(
        # 'toolroom.attribute',
    # )
    # attribute_id = fields.Many2one(
        # 'toolroom.attribute',
        # string="Atributo",
        # help="Atributo"
    # )
    # active = fields.Boolean(
        # string="Activo?"
    # )
    # product_tmpl_id = fields.Many2one(
        # string="Herramienta"
    # )




# class ToolRoomEquipmentAttributeValue(models.Model):
    # _name = 'toolroom.equipment.attribute.line'
    # _inherit = 'product.template.attribute.line'
    # _description = 'Toolroom Equipment Attribute Line'
    # _order = 'name'
    # _rec_name = 'display_name'


    # attribute_id = fields.Many2one(
        # 'toolroom.attribute',
        # string="Atributo",
        # help="Atributo"
    # )


# class ToolRoomEquipmentAttributeValue(models.Model):
    # _name = 'toolroom.equipment.attribute.value'
    # _inherit = 'product.template.attribute.value'
    # _description = 'Toolroom Equipment Attribute Value'
    # _order = 'name'
    # _rec_name = 'display_name'



