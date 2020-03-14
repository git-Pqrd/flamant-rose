from flask_sqlalchemy import SQLAlchemy
import logging as lg
from sqlalchemy.dialects.postgresql import JSON, ARRAY


from .views import app
# Create database connection object

db = SQLAlchemy(app)

#Create DB tables

class Users (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    choices = db.Column(JSON)

    def __init__(self, name, email, password, choices):
        self.name = name
        self.email = email
        self.password = password
        self.choices = choices

    def __repr__(self):
        return '<user {}>'.format(self.id)

class Menu (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    chosen_by = db.Column(ARRAY(db.String(200)))

    def __init__(self, name, chosen_by=[]):
        self.name = name
        self.chosen_by = chosen_by

    def __repr__(self):
        return '<menu {}>'.format(self.id)

class Event (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime,nullable=False)
    organizer = db.Column(db.String(200), nullable=True)

    def __init__(self, name, date, organizer=""):
        self.name = name
        self.date = date
        self.organizer = organizer

    def __repr__(self):
        return '<event {}>'.format(self.id)


#init_db can be launched using FLASK_APP=run.py flask init_db in terminal
def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Users("jean", 'jean@test.be', "password", {"entree":"rien", "plat":"rien"}))
    db.session.add(Users("charles", 'charles@test.be', "password", {"entree":"salade", "plat":"poulet"}))
    db.session.add(Users("fernand", 'fernand@test.be', "password", {"entree":"", "plat":"pizza"}))
    db.session.add(Menu("frites", ["jean", "Pierre"]))
    db.session.add(Menu("pizza", ["charles", "fernand", "rene"]))
    db.session.commit()
    lg.warning('Database initialized!')

def erase_db():
    db.drop_all()
    db.create_all()
    lg.warning("DB items cleared, tables still present")

#db.create_all()