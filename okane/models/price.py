# -*- coding: utf-8 -*-

from okane import db


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer)
    date = db.Column(db.DATE)
    open = db.Column(db.DECIMAL)
    close = db.Column(db.DECIMAL)
    high = db.Column(db.DECIMAL)
    low = db.Column(db.DECIMAL)
    volume = db.Column(db.DECIMAL)
