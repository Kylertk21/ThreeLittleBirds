from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask("Three Little Birds Web App")
app.secret_key= 'secret'
app.config['USER_SIGN_UP'] = 'User Sign Up'
app.config['USER_SIGN_IN'] = 'User Sign In'

#init Flask-SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

#init Flask-Login
login_manager = LoginManager(app)

#create database tables
with app.app_context():
    db.create_all()

#login
from app.models import User

@login_manager.user_loader
def load_user(id):
    try:
        return db.session.query(User).filter(User.id == id).one()
    except:
        return "User Not Found"
    
    
