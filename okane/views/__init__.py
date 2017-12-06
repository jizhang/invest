# -*- coding: utf-8 -*-

from okane import app


@app.route('/')
def hello_world():
    return 'Hello, World!'
