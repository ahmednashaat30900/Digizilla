
from odoo import models, fields, api
from datetime import date


class Digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _description = 'Digizilla'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(
        string='Name',
        required=True,
        tracking=True,
    )

    
    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        string='Gender',
        tracking=True,
    )

    
    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country',
        tracking=True,
    )

    
    birth_date = fields.Date(
        string='Birth Date',
        tracking=True,
    )

    
    age = fields.Float(
        string='Age',
        compute='_compute_age',
        store=True,
    )

    
    tag_ids = fields.Many2many(
        comodel_name='res.partner.category',
        string='Tags',
    )

    
    customer_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        required=True,
        tracking=True,
    )

    
    sale_order_count = fields.Float(
        string='No. of Sales Orders',
        compute='_compute_sale_order_count',
        store=True,           
        group_operator='sum',
    )

    
    notes = fields.Html(
        string='Notes',
    )

    # (x) Comments - Char
    comments = fields.Char(
        string='Comments',
    )

 
    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.birth_date:
                born = rec.birth_date
                rec.age = float(
                    today.year - born.year
                    - ((today.month, today.day) < (born.month, born.day))
                )
            else:
                rec.age = 0.0



    @api.depends('customer_id')
    def _compute_sale_order_count(self):
        for rec in self:
            if rec.customer_id:
                child_ids = self.env['res.partner'].search([
                    ('id', 'child_of', rec.customer_id.id)
                ]).ids
                rec.sale_order_count = float(
                    self.env['sale.order'].search_count([
                        ('partner_id', 'in', child_ids)
                    ])
                )
            else:
                rec.sale_order_count = 0.0

    def _recompute_sale_order_count(self, partner_ids):
        """Called by SaleOrder hooks to refresh count on affected records."""
        if not partner_ids:
            return
        records = self.search([('customer_id', 'in', partner_ids)])
        if records:
            records._compute_sale_order_count()
            # Force write so store=True field actually saves
            for rec in records:
                rec.write({'sale_order_count': rec.sale_order_count})



    def action_view_sale_orders(self):
        self.ensure_one()
        partner = self.customer_id
        child_ids = self.env['res.partner'].search([
            ('id', 'child_of', partner.id)
        ]).ids
        orders = self.env['sale.order'].search([
            ('partner_id', 'in', child_ids)
        ])
        return {
            'type': 'ir.actions.act_window',
            'name': f'Sales Orders — {partner.name}',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'domain': [('id', 'in', orders.ids)],
            'context': {
                'default_partner_id': partner.id,
                'create': True,
            },
        }


class SaleOrderDigizillaHook(models.Model):
    """
    Extend sale.order to automatically refresh sale_order_count
    on any linked Digizilla record when orders are created,
    updated, or deleted.
    """
    _inherit = 'sale.order'

    def _sync_digizilla_count(self):
        partner_ids = self.mapped('partner_id').ids
        if partner_ids:
            self.env['digizilla.digizilla']._recompute_sale_order_count(
                partner_ids
            )

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._sync_digizilla_count()
        return records

    def write(self, vals):
        result = super().write(vals)
        if 'partner_id' in vals or 'state' in vals:
            self._sync_digizilla_count()
        return result

    def unlink(self):
        self._sync_digizilla_count()
        return super().unlink()
