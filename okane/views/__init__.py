# -*- coding: utf-8 -*-

from flask import jsonify
from okane import app, db
from okane.models.stock import Stock


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/stock')
def stock():
    count = db.session.query(Stock).count()
    return jsonify(count=count)
