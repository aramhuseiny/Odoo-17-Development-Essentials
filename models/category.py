from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Category(models.Model):
    
    _name="library.category"
    _description="Category"
    name = fields.Char( string="Category Name")
    code = fields.Char( string="Code")
    
    
    @api.model
    def get_expense_dashboard(self):
        items = self.env['library.category'].search_read([])
        return items