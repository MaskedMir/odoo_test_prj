from odoo import models, fields, api
from odoo.exceptions import AccessError

class ProductThing(models.Model):
    _name = 'my.product.thing'
    _description = 'My Product Thing'

    name = fields.Char(required=True)
    production_date = fields.Date()
    color = fields.Selection([
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('white', 'White'),
    ], required=True)
    weight = fields.Float()
    user_id = fields.Many2one('res.users', default=lambda self: self.env.uid, readonly=True)

    def write(self, vals):
        if not self.env.user.has_group('my_module.group_admin'):
            for record in self:
                if record.user_id != self.env.user:
                    raise AccessError("Вы можете редактировать только свои записи.")
        return super().write(vals)

    def custom_action(self):
        # Здесь логика твоего действия
        # Пока просто заглушка
        for rec in self:
            _logger.info(f"Custom action triggered for {rec.name}")
        return True