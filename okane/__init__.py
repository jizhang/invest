# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('okane.default_settings')
app.config.from_envvar('OKANE_SETTINGS', silent=True)

db = SQLAlchemy(app)


import okane.views
import okane.commands
