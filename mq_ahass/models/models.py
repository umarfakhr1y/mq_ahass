# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mq_ahass(models.Model):
    _name = 'mq.ahass'

    name = fields.Char(string='Antrian ke', readonly=True, default="/")
    namacustomer_id = fields.Many2one('res.partner', 'Nama Customer')
    
    tanggal_masuk = fields.Date(string="Tanggal Masuk")
    name_id = fields.Many2one('res.partner', string="Nama")
    alamat = fields.Char(string="Alamat")
    kendaraan = fields.Char(string="Kendaraan")
    no_telepon = fields.Integer(string="Nomor Telepon")
    no_mesin = fields.Integer(string="No Mesin")
    km = fields.Integer(string="KM")
    no_polisi = fields.Integer(string="No Polisi")

    @api.model
    def create(self, vals):
            vals['name'] = self.env['ir.sequence'].next_by_code('mq.ahass')
            return super(mq_ahass, self).create(vals)
    
    # @api.multi
    # def name_get(self):
    #         return [(this.id, this.name + "#" + " " + this.product_id.partner_ref) for this in self]

    
    