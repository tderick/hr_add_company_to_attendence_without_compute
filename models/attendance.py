from odoo import fields, models, api


class InheritedAttendance(models.Model):
    _inherit = "hr.attendance"

    agence = fields.Char(string="Agence", compute="_compute_agence")

    def _compute_agence(self):
        for attendance in self:
            attendance.agence = self.env.user.company_id.street
