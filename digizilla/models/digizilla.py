from odoo import models, fields #type:ignore


class Digizilla(models.Model):
    _name = 'digizilla'
    _description = 'Digizilla'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(required=True, tracking=1)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], default="male", tracking=1)
    # In the country field, I prefer to use the Odoo 'res.country' model to help the user to only choose his country
    country = fields.Many2one('res.country', tracking=1)
    # Here I made the default value for the field to be the day of creation date
    # but the user can change it as he/she likes
    joining_date = fields.Date(
        default=lambda self: fields.Date.today(), tracking=1)
    # I preferred to make the relation between the field 'tag_id' and the Table 'Tag' Many2one
    # which contains unique names
    tag_id = fields.Many2one('tag', tracking=1)
    customer_ids = fields.Many2many('res.partner', tracking=1)
    company = fields.Many2one('res.company', required=True, tracking=1)
    notes = fields.Text(tracking=1)
    # I preferred to make this field from a type Text not Char so the user can write a big comment
    comments = fields.Text(tracking=1)
