# -*- coding: utf-8 -*-
# from odoo import http


# class GymManagement(http.Controller):
#     @http.route('/gym_management/gym_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gym_management/gym_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gym_management.listing', {
#             'root': '/gym_management/gym_management',
#             'objects': http.request.env['gym_management.gym_management'].search([]),
#         })

#     @http.route('/gym_management/gym_management/objects/<model("gym_management.gym_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gym_management.object', {
#             'object': obj
#         })

