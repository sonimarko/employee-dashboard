from datetime import datetime, time, date
from dateutil.relativedelta import relativedelta
from odoo import api, models, api, exceptions, fields, _

class HREmployee(models.Model):
	_inherit = 'hr.employee'

	ns_is_today_birthday = fields.Boolean(compute='_compute_ns_is_today_birthday', store=True)

	@api.depends('birthday')
	def _compute_ns_is_today_birthday(self):
		today = date.today()
		for rec in self:
			rec.ns_is_today_birthday = False
			if rec.birthday:
				if rec.birthday.day == today.day and rec.birthday.month == today.month:
					rec.ns_is_today_birthday = True

	@api.model
	def retrieve_dashboard(self):
		self.check_access_rights('read')

		result = {
			'today_birthday_count': 0,
		}

		today = date.today()
		count = 0

		po = self.env['hr.employee'].search([])
		for rec in po:
			if rec.birthday:
				if rec.birthday.day == today.day and rec.birthday.month == today.month:
					count += 1

		result['today_birthday_count'] = count

		return result