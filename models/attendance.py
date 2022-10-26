from odoo import fields, models


class InheritedAttendance(models.Model):
    _inherit = "hr.attendance"

    agence = fields.Char(string="Agence", readonly=True)
