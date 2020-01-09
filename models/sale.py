# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def test_note(self):
        return "this is test Note"
    
    test_amount = fields.Float(string="Test amount")
    payment_term_id = fields.Many2one(help="This is payment term")
    note = fields.Text(default=test_note)
    purchase_date=fields.Date(string="Purchase Date")
    