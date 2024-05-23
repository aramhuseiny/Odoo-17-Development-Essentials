from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    
    _name="library.book"
    _description="Book"
    name = fields.Char( string="Book Name")
    isbn = fields.Char( string="Book ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner",string="Publisher")
    author_ids = fields.Many2many("res.partner",string="Authors")
    category_ids = fields.Many2many("library.category",string="Categories")
    reference_no = fields.Char(string='Book Reference', required=True,
                          readonly=True, default=lambda self: ('New'))
    
    
    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12],ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check
        
        
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError("Please provide an ISBN for %s" % book.name)
            if book.isbn and not book._check_isbn():
                raise ValidationError("%s ISBN is invalid" % book.isbn)
            return True
        
        
    @api.model
    def create(self, vals):
        if vals.get('reference_no', ('New')) == ('New'):
            vals['reference_no'] = self.env['ir.sequence'].next_by_code(
                'library.book') or ('New')
        res = super(Book, self).create(vals)
        return res