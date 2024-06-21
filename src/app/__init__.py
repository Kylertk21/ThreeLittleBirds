from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads
import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = os.path.join(os.getcwd(), 'static/photos')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback_secret_key')

print("Photos DIR: ", os.path.join(os.getcwd(), 'static/photos'))
print("Work DIR: ", os.getcwd())
template_dir = os.path.join(os.getcwd(), 'templates')

app = Flask("Three Little Birds", template_folder=template_dir)
app.static_folder = 'static' 
app.secret_key = os.environ['SECRET_KEY']
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)


photos = UploadSet('photos', ('png', 'jpg', 'jpeg'))
configure_uploads(app, photos)



from . import routes
