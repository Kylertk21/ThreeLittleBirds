from . import app, db
from flask import render_template, url_for, request, flash
from .forms import ItemForm
from .models import Item
import uuid

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marketplace')
def marketplace():
    items = Item.query.all()
    return render_template('marketplace.html', items=items)

@app.route('/add_item', methods=['GET','POST'])
def add_item():
    form = ItemForm()
    if request.method =='POST':
        if form.validate_on_submit():
            item = Item(
                id=str(uuid.uuid4()),
                name=form.name.data,
                quantity=form.quantity.data,
                description=form.description.data,
                price=form.price.data
                image=form.image.data
            )

            file = request.files['image']
            if file.filename == '':
                flash("No Image Provided")
                return render_template('add_item.html', form=form)
            
            db.session.add(item)
        flash("Item added successfully")
    else: flash(form.errors, 'error')
    db.session.commit()
    return render_template('add_item.html', form=form)

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