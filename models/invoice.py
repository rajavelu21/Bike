# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'
     
    
    invoice_no = fields.Integer(string="Invoice Number")
    invoice_type = fields.Text(string="Invoice Type")