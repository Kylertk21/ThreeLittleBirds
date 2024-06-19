from . import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marketplace')
def marketplace():
    catalog_items = [
        {'image':'../static/photos/logo_placeholder.jpg', 'description':'Item', 'link':'/orderform'}
    ]

    return render_template('marketplace.html', catalog_items=catalog_items)

@app.route('/add_item')
def add_item():
    return render_template('add_item.html')

@app.route('/orderform')
def orderform():
    return render_template('orderform.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')