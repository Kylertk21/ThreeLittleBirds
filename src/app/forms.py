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