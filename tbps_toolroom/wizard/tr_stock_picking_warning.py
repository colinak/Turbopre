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


class TrStockPickingWarningWizard(models.TransientModel):
    _name = 'tr.stock.picking.warning.wizard'
    _description = 'Advertencia de Herramienta Asignada'

    message = fields.Text(readonly=True)
    picking_id = fields.Many2one('tr.stock.picking')

    def action_confirm(self):
        # Aquí pones la lógica que se ejecuta si el usuario da clic en "Continuar"
        return self.picking_id.with_context(skip_check=True).return_confirm()
        # return self.picking_id.return_confirm()

