from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit ='sale.order'

    ahass_id = fields.Many2one('res.partner', 'Antrian')
    