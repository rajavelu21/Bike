# -*- coding: utf-8 -*-

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
     
    
    joining_date = fields.Date(string="Joining Date")
 
    