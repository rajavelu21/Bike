# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo.exceptions import ValidationError
from odoo import models, fields, api, _
 
import re

class BikeRepire(models.Model):
    _name = 'bike_repire.bike_repire'
    _inherit = 'mail.thread'
    _description = 'Bike Report'
    _rec_name = 'bike_name'

    bike_name = fields.Char(string='Bike name', required=True , track_visibility="always")
    bike_no = fields.Char('Bike number', track_visibility="always")
    note = fields.Text('Notes')
    bike_image = fields.Binary('Image') 
    bike_seq = fields.Char(string='Bike sequence', required=True , copy=False, readonly=True, index=True, default=lambda self:_('New'))
    customer_name = fields.Many2many('res.users',string="Customer Name")
    color = fields.Integer("Color Index", default=0)
    blue=fields.Boolean("Blue")
    pink=fields.Boolean("Pink")
    yellow=fields.Boolean("Yellow")
    start_date=fields.Date(default=fields.Date.today)
    date_end=fields.Date(string="End date",store=True,compute='_get_end_date', inverse='_set_end_date')
    duration=fields.Float(digits=(6, 2), help="Duration in days")
    
    
    @api.model
    def create(self,vals):
        if vals.get('bike_seq',_('New')) == _('New'):
            vals['bike_seq'] = self.env['ir.sequence'].next_by_code('bike.repire.sequence') or _('New')
            result = super(BikeRepire, self).create(vals)
            return result
        
        
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.date_end=r.start_date
                continue
            duration = timedelta(days=r.duration,seconds=-1)
            r.date_end = r.start_date + duration
    
    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.date_end):
                continue
            r.duration = (r.date_end - r.start_date).days + 1
                
    
    
class BikeBooking(models.Model):
    _name = 'bike.booking'
    _rec_name = 'boking_title'
    

    booking_id = fields.Text(string='Booking Id')
    boking_title = fields.Text('Booking Title')
    booking_type = fields.Text('Booking type')
    booking_date = fields.Date('Booking Date')
    booking_desc = fields.Text('Booking note')


class BikeInsurance(models.Model):
    _name = 'bike.insurance_renew'
    _rec_name='insurance_bike_id'    

    insurance_id = fields.Integer(string='Insurance Id')
    insurance_bike_id = fields.Text('Insurance Bike_id')
    insurance_number = fields.Integer('Insurance Number')
    insurance_date = fields.Date('Insurance Date')
    insurance_expiry = fields.Date('Insurance Expiry')
    insurance_amount = fields.Text(string='Insurance Amount')
    insurance_type = fields.Char('Insurance Type')
    insurance_desc = fields.Text('Insurance Decs.')
    
    
class BikeCustomer(models.Model):
    _name ='bike.customer'
    _rec_name='customer_id'
    
    customer_id = fields.Integer(string='Customer Id')
    customer_name = fields.Char('Customer Name')
    customer_mobile = fields.Text('Mobile No')
    customer_email = fields.Text('Email')
    customer_address = fields.Text('Address')
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other'),],default='male')
    
    
    @api.onchange('customer_email')
    def validation_mail(self):
        match=0
        if self.customer_email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.customer_email)
        if match == None:
            raise ValidationError('Not a valid E-mail ID')
    
    @api.constrains('customer_mobile')
    def _check_phone_number(self):
        for rec in self:
            if rec.customer_mobile and len(rec.customer_mobile) != 10:
                raise ValidationError(_("Not a valid Mobile Number"))
                return True
    
class QueryCustomer(models.Model):
    _name = 'query.customer'
    
    query_id = fields.Integer(string='Query Id')
    query_name = fields.Text('Query Desc')
    query_type = fields.Text('Query Type')
    customer_name = fields.Text('Customer Name')
    customer_no = fields.Text('Customer Number')