# -*- coding: utf-8 -*-

from okane import app, db
from okane.models.stock import Stock


@app.cli.command()
def fetch_data():
    rows = db.session.query(Stock).all()
    print(len(rows))
