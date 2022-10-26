# -*- coding: utf-8 -*-
# from odoo import http


# class AddCompanyToAttendence(http.Controller):
#     @http.route('/add_company_to_attendence/add_company_to_attendence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_company_to_attendence/add_company_to_attendence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_company_to_attendence.listing', {
#             'root': '/add_company_to_attendence/add_company_to_attendence',
#             'objects': http.request.env['add_company_to_attendence.add_company_to_attendence'].search([]),
#         })

#     @http.route('/add_company_to_attendence/add_company_to_attendence/objects/<model("add_company_to_attendence.add_company_to_attendence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_company_to_attendence.object', {
#             'object': obj
#         })
