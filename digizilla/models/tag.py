from odoo import models, fields  # type:ignore


class Tag(models.Model):
    _name = 'tag'
    _description = 'Tag'

    name = fields.Char()
    digizilla_ids = fields.One2many('digizilla', 'tag_id')

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'Tag must be unique!')
    ]