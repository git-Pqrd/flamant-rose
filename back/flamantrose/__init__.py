import os
from flask import Flask

from flamantrose.views import app
from . import models

# Connect sqlalchemy to app

models.db.init_app(app)

@app.cli.command('init_db')
def init_db():
    models.init_db()
@app.cli.command('erase_db')
def erase_db():
    models.erase_db()