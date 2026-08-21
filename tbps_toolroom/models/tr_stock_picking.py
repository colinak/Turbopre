#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
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

class TrStockPicking(models.Model):
    _name = 'tr.stock.picking'
    _description = 'Toolroom Operaciones'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Referencia",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('Nuevo')
    )
    company_id = fields.Many2one(
        "res.company",
        string="Compañia"
    )
    date = fields.Datetime(
        string="Fecha",
        default=fields.Datetime.now,
        index=True,
        required=True,
        help="Fecha programada hasta que se realiza el movimiento, luego fecha de procesamiento del movimiento real"
    )
    location_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación origen",
    )
    location_dest_id = fields.Many2one(
        "tr.stock.location",
        string="Ubicación destino",
    )
    move_lines = fields.One2many(
        "tr.stock.move",
        "picking_id",
        string="Movimientos de stock"
    )
    move_line_ids = fields.One2many(
        "tr.stock.move.line",
        "picking_id",
        string="Operaciones"
    )
    picking_type_code = fields.Selection(
        selection=[
            ('assignment', 'Asignación'),
            ('loans', 'Prestamo'),
            ('reception', 'Devolución'),
            ('transfers', 'Transferencias')
            # ('discard', 'Desechar'),
        ],
        string='Tipo de Operación',
        required=True,
        default="loans"
    )
    product_id = fields.Many2one(
        "product.product",
        string="Producto"
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Contacto"
    )
    user_id = fields.Many2one(
        "res.users",
        string="Usuario"
    )
    note = fields.Text(
        string="Notas"
    )
    signature_applicant = fields.Char(
        string="PIN Solicitante"
    )
    applicant_id = fields.Many2one(
        "hr.employee",
        string="Solicitante",
        ondelete="RESTRICT"
    )
    signature_deliverer = fields.Char(
        string="PIN quien Entrega"
    )
    delivery_id = fields.Many2one(
        "hr.employee",
        string="Entrega",
        ondelete="RESTRICT"
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('prepared', 'Reservado'),
            ('done', 'Validado'),
            ('cancel', 'Cancelado'),
        ],
        string="Estado",
        default="draft"
    )
    count_line = fields.Integer(
        string="Lineas de Herramientas",
        compute="_compute_count_line"
    )
    count_move_lines = fields.Integer(
        string="Lineas de Herramientas",
    )
    availability = fields.Boolean("Availability", default=False)


    def _compute_count_line(self):
        for line in self:
            line.count_line = len(line.move_line_ids)

    
    @api.onchange('move_lines')
    def _onchange_count_move_lines(self):
        if self.move_lines:
            self.count_move_lines = len(self.move_lines)


    @api.onchange('signature_applicant')
    def _onchange_signature_applicant(self):
        if self.signature_applicant:
            applicant = self.env['hr.employee'].search(
                [('pin', '=', self.signature_applicant)],
                limit=1
            )
            if len(applicant) < 1:
                self.signature_applicant = ""
                self.applicant_id = ""
                raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")
            else:
                self.applicant_id = applicant.id



    @api.onchange('signature_deliverer')
    def _onchange_deliverer_signature(self):
        if self.signature_deliverer:
            deliverer = self.env['hr.employee'].search(
                [('pin', '=', self.signature_deliverer)],
                limit=1
            )
            if len(deliverer) < 1:
                self.signature_deliverer = ""
                self.delivery_id = ""
                raise UserError("Error, No se encontro ningún empleado Con ese código PIN, por favor verifíque e intente de nuevo.")
            else:
                self.delivery_id = deliverer.id


    def action_cancel_draft(self):
        pass


    def assigned_confirm(self):
        for line in self.move_line_ids:
            try:
                line.reference = self.name
                line.state = "done"
                line.lot_id.write({
                    'location_id': self.location_dest_id.id,
                    'stage': "assigned",
                    'employee_id': self.applicant_id.id,
                    'assigned_date': self.date
                })
                quants = self.env['tr.stock.quant'].search([
                    ('lot_id', '=', line.lot_id.id)
                ])
                quants.write({
                    'location_id': self.location_dest_id.id,
                    'inventory_quantity': 1
                })
            except:
                raise UserError("¡Error al intentar asignación!")


    
    def loan_confirm(self):
        for line in self.move_line_ids:
            try:
                line.reference = self.name
                line.state = "done"
                line.lot_id.write({
                    'location_id': self.location_dest_id.id,
                    'stage': "loan",
                    'employee_id': self.applicant_id.id,
                    'assigned_date': self.date
                })
                quants = self.env['tr.stock.quant'].search([
                    ('lot_id', '=', line.lot_id.id)
                ])
                quants.write({
                    'location_id': self.location_dest_id.id,
                    'inventory_quantity': 1
                })
            except:
                raise UserError("¡Error al intentar devolución!")

    def action_check_stage(self):

        # Verificar si ya aceptamos el riesgo anteriormente
        if self.env.context.get('skip_check'):
            return self.sudo().return_confirm()

        # Buscamos si hay alguna línea con herramienta asignada
        assigned_lines = self.move_line_ids.filtered(lambda l: l.lot_id.stage == 'assigned')

        if assigned_lines:
            _logger.info("Se encontraron líneas asignadas, lanzando Wizard")
            names = ", ".join(assigned_lines.mapped('lot_name'))
            return {
                'name': 'Advertencia: Herramienta Asignada',
                'type': 'ir.actions.act_window',
                'res_model': 'tr.stock.picking.warning.wizard',
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'default_picking_id': self.id,
                    'default_message': f'La herramienta {names} está asignada. ¿Deseas continuar de todas formas?',
                }
            }
        return self.sudo().return_confirm()

    def return_confirm(self):
        for line in self.move_line_ids:
            try:
                line.reference = self.name
                line.state = "done"
                line.lot_id.write({
                    'location_id': line.location_dest_id.id,
                    'stage': "available",
                    'employee_id': False,
                    'assigned_date': self.date
                })
                quants = self.env['tr.stock.quant'].search([
                    ('lot_id', '=', line.lot_id.id)
                ])
                quants.write({
                    'location_id': line.location_dest_id.id,
                    'inventory_quantity': 1
                })
            except:
                raise UserError("¡Error al intentar devolver herramienta!")
            self.state = "done"


    def transfer_confirm(self):
        """
        Confirma la transferencia de herramientas, valida disponibilidad y genera los movimientos.
        """
        try:
            if not self.move_line_ids:
                raise UserError("No hay herramientas registradas para transferir.")

            # 1 Lógica de movimiento de inventario (Creación de Stock Moves nativos si aplica)
            # Para que Odoo mueva el inventario de location_id a location_dest_id, 
            # lo correcto es generar un registro en 'stock.move' o 'stock.move.line' nativo de Odoo.
            
            stock_move_line_obj = self.env['tr.stock.move.line']

            for line in self.move_line_ids:
                # Registramos el movimiento físico en el inventario real de Odoo
                line.name = self.name
                line.lot_id.write({
                    'location_id': self.location_dest_id.id or line.location_dest_id.id,
                    'employee_id': self.delivery_id.id or False,
                    'assigned_date': self.date
                }),
                quants = self.env['tr.stock.quant'].search([
                    ('lot_id', '=', line.lot_id.id)
                ])
                quants.write({
                    'location_id': self.location_dest_id.id,
                    'inventory_quantity': 1
                })

                stock_move_line_obj.create({
                    'lot_id': line.lot_id.id,
                    'product_id': line.product_id.id,
                    'product_uom_id': line.product_id.uom_id.id,
                    'location_id': line.location_id.id,
                    'location_dest_id': line.location_dest_id.id,
                    'qty_done': 1.0,  # Tratándose de herramientas con número de serie específico
                })
                line.state = "done"

        except:
            raise UserError("¡Error al intentar transferencia de herramientas!")

        self.state = "done"
        # return True


    def action_assign(self):
        for move in self.move_lines:
            if move.product_uom_qty > move.product_availability:
                raise UserError(f"La cantidad demandada para {move.product_id.name} es mayor a la disponible")
            else:
                self.write({'availability': True})


    def action_reserve(self):
        for move in self.move_line_ids:
            move.lot_id.write({
                'stage': "reserved"
            })
        self.write({'state': "prepared"})


    @api.model
    def check_duplicate_records(self):
        viewed = set()
        for line in self.move_line_ids:
            if self.picking_type_code == 'loans' and line.lot_id.stage != 'available':
                raise UserError(f"¡Error! \nEsta herramienta {line.lot_name} ya se encuentra prestada")
            elif self.picking_type_code == 'assignment' and line.lot_id.stage != 'available':
                raise UserError(f"¡Error! \nEsta herramienta {line.lot_name} ya se encuentra asignada")
            elif self.picking_type_code == 'reception' and line.lot_id.stage == 'available':
                raise UserError(f"¡Error! \nEsta herramienta {line.lot_name} no se encuentra prestada")
            elif line.lot_name in viewed:
                raise UserError(f"¡Error!\nSe consiguieron registros duplicados {line.lot_name}")
            else:
                viewed.add(line.lot_name)
        return True


    def action_validate(self):
        if self.applicant_id == self.delivery_id:
            raise UserError("¡Error!\n No es posible solicitar y entregar una herramienta al mismo tiempo.")
        elif len(self.move_line_ids) < 1:
            raise UserError(f"¡Error!\n No es posible validar un {self.picking_type_code} sin lineas de herramientas.")
        elif self.check_duplicate_records():
            try:
                if self.name == 'Nuevo':
                    if self.picking_type_code == "assignment":
                        self.name = self.env['ir.sequence'].next_by_code('tr.stock.picking.assignment') or _('Nuevo')
                        self.sudo().assigned_confirm()
                        self.state = "done"
                    elif self.picking_type_code == "loans":
                        self.name = self.env['ir.sequence'].next_by_code('tr.stock.picking.loans') or _('Nuevo')
                        self.sudo().loan_confirm()
                        self.state = "done"
                    elif self.picking_type_code == "reception":
                        self.name = self.env['ir.sequence'].next_by_code('tr.stock.picking.returns') or _('Nuevo')
                        return self.action_check_stage()
                        # self.sudo().return_confirm()
                    elif self.picking_type_code == "transfers":
                        self.name = self.env['ir.sequence'].next_by_code('tr.stock.picking.transfers') or _('Nuevo')
                        self.sudo().transfer_confirm()
                        self.state = "done"
            except:
                raise UserError("¡Error al intentar validar!")


