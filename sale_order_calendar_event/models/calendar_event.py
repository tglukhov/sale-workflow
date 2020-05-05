# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    sale_order_id = fields.Many2one('sale.order', name='Sale order')
