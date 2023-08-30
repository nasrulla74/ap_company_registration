# -*- coding: utf-8 -*-
from odoo import fields, models

class ApCompanyObjectives(models.Model):
    _name = "ap.company.obj"
    _description = "Company Objectives"

    name = fields.Char(string="Objective", required=True)
    obj_code = fields.Char(string="Code")


class ApCompanyPartner(models.Model):
    _inherit = 'res.partner'

    is_director = fields.Boolean('Is Director', default=False)
    com_reg_id = fields.Many2one('ap.company.reg', string="Company")
    witness_id = fields.Many2one('ap.company.reg', string="Witness")
    id_card_no = fields.Char(string="Id Card No")

class ApCompanyReg(models.Model):
    _name = "ap.company.reg"
    _description = "Company Registration"

    name = fields.Char(string="Company Name", required=True)
    members_limit = fields.Char(string="Members Limit")
    quorum = fields.Char(string="Quorum")
    registered_address = fields.Html(string="Registered Address")
    face_value = fields.Integer(string="Face Value", default=100)
    no_of_shares = fields.Integer(string="No of Shares", default=100)
    capital = fields.Integer(string="Capital", default=10000)
    capital_text = fields.Char(string="Capital Text")
    share_text = fields.Char(string="Share Text")
    apply_date = fields.Date(string="Date")
    director_ids = fields.One2many('res.partner', 'com_reg_id', string="Director")
    witness_ids = fields.One2many('res.partner', 'witness_id', string="Witness")
    objective_ids = fields.Many2many('ap.company.obj', string="Objectives", index=True)





