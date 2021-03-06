from wtforms import StringField, SubmitField, RadioField, SelectField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from app.amentities import ammenity

class InputForm(FlaskForm):
    
    state = SelectField(validators=[DataRequired()], choices=[], label='Please select a state:') 
    submit = SubmitField(label='Submit')

class DataForm(FlaskForm):
    region = SelectField(choices=[], label='Region')
    home_type = SelectField(choices=[i.title() for i in ammenity['house_type']], label='Home Type')
    sqfeet = StringField(validators=[DataRequired()], label='Square Footage', render_kw={'placeholder': 'Square feet (e.g., 1000)'})
    bed = SelectField(validators=[DataRequired()], choices=[i for i in range(0,5)], label='Number of Beds (0 = Studio)')
    bath = SelectField(validators=[DataRequired()], choices=[i for i in range(1, 5)], label='Number of Bathrooms')
    parking = SelectField(choices=[i.title() for i in ammenity['parking']])
    laundry = SelectField(choices=[i.title() for i in ammenity['laundry']])
    pet = RadioField(validators=[DataRequired()], choices=['Yes', 'No'], label='Pets', default='No')
    smoke = RadioField(validators=[DataRequired()], choices=['Yes', 'No'], label='Smoke', default='No')

    submit = SubmitField(label='Submit')
