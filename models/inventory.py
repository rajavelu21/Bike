# -*- coding: utf-8 -*-

from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'
     
    
    document_date = fields.Date(string="Document Date")
 
    