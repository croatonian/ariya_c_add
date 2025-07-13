# -*- coding: utf-8 -*-

from odoo import models, fields, api
class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'

    # @api.depends('holiday_status_id')

    reason = fields.Many2one(comodel_name='reason_for_leave', string="Мета вiдрядження:")
    location = fields.Many2one(comodel_name='res.country.state', string="Куди вiдрядження:")
    # lt = self.env['hr.leave.type']
    leave_type_name = fields.Char(related='holiday_status_id.name')
    employee_buh_id = fields.Integer(related='employee_id.buh_id')
    reason_name = fields.Char(related='reason.name')
    location_name = fields.Char(related='location.name')


# _sql_constraints = [
#         ('uniq_name', 'unique(your_field_name)', "You Entered data is already exists with this name. Please give data must be unique!"),
#     ]


