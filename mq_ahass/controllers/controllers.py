# -*- coding: utf-8 -*-
from odoo import http

# class MqAhass(http.Controller):
#     @http.route('/mq_ahass/mq_ahass/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mq_ahass/mq_ahass/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mq_ahass.listing', {
#             'root': '/mq_ahass/mq_ahass',
#             'objects': http.request.env['mq_ahass.mq_ahass'].search([]),
#         })

#     @http.route('/mq_ahass/mq_ahass/objects/<model("mq_ahass.mq_ahass"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mq_ahass.object', {
#             'object': obj
#         })