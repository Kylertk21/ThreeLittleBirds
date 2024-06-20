from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.LargeBinary)

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column('ID', db.String, primary_key=True)
    name = db.Column('Name', db.String)
    quantity = db.Column('Quantity', db.Integer)
    description = db.Column('Description', db.String)
    price = db.Column('Price', db.String)
    image = db.Column("Image", db.String, default='No Image')