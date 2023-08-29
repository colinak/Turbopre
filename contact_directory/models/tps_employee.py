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


class TpsEmployee(models.Model):
    _name = 'tps.employee'
    _description = 'Employee Turbopre'
    _order = 'name'
    _rec_name = 'name'


    name = fields.Char(
        string="Nombre",
        required=True,
        held="Nombre del empleado"
    )
    image_1920 = fields.Binary(
        string="Imagen"
    )
    job_id = fields.Many2one(
        "hr.job",
        # required=True,
        string="Puesto de trabajo"
    )
    department_id = fields.Many2one(
        "hr.department",
        # required=True,
        string="Departamento"
    )
    parent_id = fields.Many2one(
        "tps.employee",
        # required=True,
        string="Gerente de área",
        held="Seleccione el empleado que es el gerente de este departamento."
    )
    coach_id = fields.Many2one(
        "tps.employee",
        # required=True,
        string="Supervisor inmediato",
        held="Seleccione el empleado que es el supervidor de este empleado."
    )
    # gender = fields.Selection(

    # )
    pin = fields.Char(
        string="Código PIN",
        # required=True,
        held="PIN utilizado para registrar prestamos y devoluciones"
    )
    barcode = fields.Char(
        string="ID de credencial",
        # required=True,
        held="ID utilizado para identificar al empleado."
    )
    # active = fields.Boolean(
        # string="Activo?",
        # default=True,
    # )

