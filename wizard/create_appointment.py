# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class CreateAppointment(models.TransientModel):
    _name='create.appointment'

    customer_id=fields.Many2one('bike.customer','Customer Id')
    appointment_date=fields.Date('Appointment Date')
