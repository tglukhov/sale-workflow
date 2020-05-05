# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    calendar_event_ids = fields.One2many(
        'calendar.event', 'sale_order_id', name='Appointments')
