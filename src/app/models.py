from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column('ID', db.Integer, primary_key=True)
    name = db.Column('Name', db.String)
    password = db.Column('Password', db.LargeBinary)

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column('ID', db.String, primary_key=True)
    name = db.Column('Name', db.String)
    quantity = db.Column('Quantity', db.Integer)
    description = db.Column('Description', db.String)
    price = db.Column('Price', db.String)
    image = db.Column("Image", db.String, default='No Image')

class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column('ID', db.String, primary_key=True)
    name = db.Column('Name', db.String)
    address = db.Column('Address', db.String)
    service = db.Column('Service', db.String)
    phone = db.Column('Phone', db.String)
    