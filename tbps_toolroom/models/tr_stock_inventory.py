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

class TrStockInventory(models.Model):
    _name = 'tr.stock.inventory'
    _description = 'Toolroom Inventario'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Nombre",
        default="Inventario",
        required=True,
        states={'draft': [('readonly', False)]}
    )
    date = fields.Date(
        string="Fecha de inventario",
        readonly=True,
        default=fields.Datetime.now,
    )
    activity_user_id = fields.Many2one(
        "res.users",
        string="Usuario responsable",
        default=lambda self: self.env.user
    )
    line_ids = fields.One2many(
        "tr.stock.inventory.line",
        "inventory_id",
        string="Lineas de Inventario",
        # states={'done': [('readonly', True)]}
    )
    move_ids = fields.One2many(
        "tr.stock.move",
        "inventory_id",
        string="Movimientos creados",
        # states={'done': [('readonly', True)]}
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('confirm', 'En Progreso'),
            ('done', 'Validado'),
            ('cancel', 'Cancelada'),
        ],
        string="Estado",
        default="draft"
    )
    company_id = fields.Many2one(
        'res.company', 
        string="Company",
        readonly=True, index=True, required=True,
        # states={'draft': [('readonly', False)]},
        default=lambda self: self.env.company
    )
    location_ids = fields.Many2many(
        'tr.stock.location', 
        string='Ubicaciones',
        readonly=True, 
        # check_company=True,
        # states={'draft': [('readonly', False)]},
        domain="[('company_id', '=', company_id), ('usage', 'in', ['internal'])]"
    )
    product_ids = fields.Many2many(
        'product.product', 
        string='Productos', 
        # check_company=True,
        domain="[('type', '=', 'product')]", 
        # readonly=True,
        # states={'draft': [('readonly', False)]},
        help="Especifique Productos para enfocar su inventario en Productos particulares.")


    def action_start(self):
        self.ensure_one()
        self._action_start()
        return self.action_open_inventory_lines()
        pass


    def _action_start(self):
        """ Confirma el Ajuste de Inventario y genera sus líneas de inventario.
        si su estado es borrador y aún no tiene líneas de inventario (puede 
        suceder con datos de demostración o pruebas).action_start
        """
        for inventory in self:
            if inventory.state != 'draft':
                continue
            vals = {
                'state': 'confirm',
                'date': fields.Datetime.now()
            }
            inventory.write(vals)


    def action_open_inventory_lines(self):
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'name': _('Lineas de Inventario'),
            'res_model': 'tr.stock.inventory.line',
        }
        # Define domains and context
        context = {
            'default_is_editable': True,
            'default_inventory_id': self.id,
            'default_company_id': self.company_id.id,
        }
        
        domain = [
            ('inventory_id', '=', self.id),
            ('location_id.usage', 'in', ['internal', 'transit'])
        ]

        action['view_id'] = self.env.ref('tbps_toolroom.view_stock_inventory_line_tree').id
        action['context'] = context
        action['domain'] = domain
        return action

    def action_cancel_draft(self):
        # self.mapped('move_ids')._action_cancel()
        self.line_ids.unlink()
        self.write({'state': 'draft'})


    def action_validate(self):
        pass




class TrStockInventoryLine(models.Model):
    _name = 'tr.stock.inventory.line'
    _description = 'Toolroom Linea de Inventario'
    _order = "product_id, inventory_id, location_id, prod_lot_id"
    _rec_name = 'name'


    name = fields.Char(
        string="Nombre"
    )
    display_name = fields.Char(
        string="Mostrar nombre"
    )
    inventory_date = fields.Datetime(
        string="Fecha del inventario"
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto",
    )
    prod_lot_id = fields.Many2one(
        "tr.stock.production.lot",
        string="N° de Serie"
    )
    product_qty = fields.Integer(
        string="Cantidad",
        default=1
    )
    product_uom_id = fields.Many2one(
        "uom.uom",
        string="Unidad de medida",
        related="product_id.uom_id",
        readonly="True"
    )
    category_id = fields.Many2one(
        "product.category",
        string="Categoría de producto"
    )
    inventory_id = fields.Many2one(
        "tr.stock.inventory",
        string="Inventario"
    )
    theoretical_qty = fields.Integer(
        string="A mano",
        related="product_id.available_qty",
        readonly="True"
    )
    difference_qty = fields.Integer(
        string="Diferencia"
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Propietario"
    )
    inventory_date = fields.Date(
        string="Fecha del inventario"
    )
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación",
        default=lambda self: self.env['tr.stock.location'].search([
            ('default_location', '=', True)
        ])
    )
    company_id = fields.Many2one(
        "res.company",
        string=u"Compañia",
        related="inventory_id.company_id"
    )
    state = fields.Selection(
        string="Estado",
        related='inventory_id.state'
    )
    inventory_date = fields.Datetime(
        string = "Fecha del inventario",
        default= fields.Datetime.now(),
        help=u"Última fecha en que se calculó la cantidad disponible."
    )
