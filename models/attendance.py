from odoo import fields, models, api


class InheritedAttendance(models.Model):
    _inherit = "hr.attendance"

    agence = fields.Char(string="Agence")


