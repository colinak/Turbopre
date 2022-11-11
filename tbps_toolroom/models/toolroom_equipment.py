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

class TrProductTemplate(models.Model):
    _inherit = 'product.template'
    # _name = 'tr.product.template'
    # _description = 'Toolroom Equipment'
    # _order = 'name'
    # _rec_name = 'name'


    # name = fields.Char(
        # string="Name",
    # )
    # category_id = fields.Many2one(
        # 'toolroom.category',
        # string="Product Category",
        # required=True,
        # help="Seleccionar categoría para el producto actual"
    # )
    # route_ids = fields.Many2many(
        # 'stock.location.route',
        # 'tr_stock_route_equipment_rel',
        # 'equipment_id',
        # 'route_id',
        # string="Rutas"
    # )
    # product_variant_id = fields.Many2one(
        # 'tr.product.product',
        # string="Herramienta"
    # )
    # product_variant_ids = fields.One2many(
        # 'tr.product.template',
        # 'product_tmpl_id',
        # string="Herramientas"
    # )
    # taxes_id = fields.Many2many(
        # 'account.tax',
        # 'tr_product_taxes_rel',
        # 'equipment_id',
        # 'tax_id',
        # string="Impuestos"
    # )
    # supplier_taxes_id = fields.Many2many(
        # 'account.tax',
        # 'tr_product_supplier_taxes_rel',
        # 'equipment_id',
        # 'tax_id',
        # string="Impuestos"
    # )


    # identification_code = fields.Char(string="Identification Code")
    # location = fields.Char(string="Location")
    # serial_number = fields.Char(string="Serial Number")



# class TrProductProduct(models.Model):
	# _inherit = 'product.product'
	# _name = 'tr.product.product'
	# _description = 'Toolroom Tools'
	# _order = 'name'
	# _rec_name = 'name'


	# name = fields.Char(
		# string="Name",
	# )
	# category_id = fields.Many2one(
		# 'toolroom.category',
		# string="Product Category",
		# required=True,
		# help="Seleccionar categoría para el producto actual"
	# )
	# route_ids = fields.Many2many(
		# 'stock.location.route',
		# 'tr_stock_route_tools_rel',
		# 'tool_id',
		# 'route_id',
		# string="Rutas"
	# )   
    # product_tmpl_id = fields.Many2one(
        # 'tr.product.template',
        # string="Herramienta",
        # help="Plantilla de producto"
    # )
    # product_variant_id = fields.Many2one(
        # 'tr.product.product',
        # related='product_tmpl_id.product_variant_id',
        # string="Herramienta"
    # )
    # product_variant_id = fields.One2many(
        # 'tr.product.template',
        # 'product_tmpl_id',
        # related='product_tmpl_id.product_variant_ids',
        # string="Herramientas"
    # )
    # product_template_attribute_value_ids = fields.Many2many(
        # 'toolroom.equipment.attribute.value',
        # 'tr_equipment_attribute_value_rel',
        # 'equipment_id',
        # 'attribure_id',
        # string="Valores de atributo",
        # help="Valores de atributo"
    # )


