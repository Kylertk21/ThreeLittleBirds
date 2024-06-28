from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, FileField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = DecimalField('Quantity', validators=[DataRequired()])
    description = StringField('Description')
    price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')
    image = FileField('Image')

class ServiceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"class": "form-control"})
    address = StringField('Address', validators=[DataRequired()], render_kw={"class": "form-control"})
    service = StringField('Service', validators=[DataRequired()], render_kw={"class": "form-control"})
    phone = StringField('Phone', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})