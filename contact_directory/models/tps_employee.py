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
    job_id = fields.Many2one(
        "hr.job",
        required=True,
        string="Puesto de trabajo"
    )
    department_id = fields.Many2one(
        "hr.department",
        required=True,
        string="Departamento"
    )
    parent_id = fields.Many2one(
        "tps.employee",
        string="Gerente de área",
        held="Seleccione el empleado que es el gerente de este departamento."
    )
    coach_id = fields.Many2one(
        "tps.employee",
        string="Supervisor inmediato",
        held="Seleccione el empleado que es el supervidor de este empleado."
    )
    pin = fields.Char(
        string="Código PIN",
        required=True,
        held="PIN utilizado para registrar prestamos y devoluciones"
    )
    barcode = fields.Char(
        string="ID de credencial",
        required=True,
        held="ID utilizado para identificar al empleado."
    )
    active = fields.Boolean(
        string="Activo?",
        default=True,
    )

    # all image fields are base64 encoded and PIL-supporte
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)

    # resized fields stored (as attachment) for performance
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)

    _sql_constraints = [
        ('barcode_uniq', 'unique (barcode)', "El ID de la Credencial debe ser único, éste ya está asignado a otro empleado."),
        ('pin_uniq', 'unique (pin)', "El Código PIN debe ser único, éste ya está asignado a otro empleado.")
    ]

