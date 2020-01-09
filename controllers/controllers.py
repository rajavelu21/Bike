# -*- coding: utf-8 -*-
from odoo import http

# class BikeRepire(http.Controller):
#     @http.route('/bike_repire/bike_repire/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bike_repire/bike_repire/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bike_repire.listing', {
#             'root': '/bike_repire/bike_repire',
#             'objects': http.request.env['bike_repire.bike_repire'].search([]),
#         })

#     @http.route('/bike_repire/bike_repire/objects/<model("bike_repire.bike_repire"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bike_repire.object', {
#             'object': obj
#         })