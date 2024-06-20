from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://kyler:icedog@localhost/tlb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

print("Work DIR: ", os.getcwd())
template_dir = os.path.join(os.getcwd(), 'templates')

app = Flask("Three Little Birds", template_folder=template_dir)
app.secret_key = os.environ['SECRET_KEY']
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

with app.app_context():
    db.create_all()


from . import routes
