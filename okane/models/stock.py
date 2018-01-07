# -*- coding: utf-8 -*-

from okane import db


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)
    name = db.Column(db.String)
    is_index = db.Column(db.Integer, default=0)
