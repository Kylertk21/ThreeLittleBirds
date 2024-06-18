from flask import Flask
import os

print("Work DIR: ", os.getcwd())

template_dir = os.path.join(os.getcwd(), 'templates')
print("Template folder: ", template_dir)

app = Flask("Three Little Birds", template_folder=template_dir)
app.secret_key = os.environ['SECRET_KEY']

from . import routes
