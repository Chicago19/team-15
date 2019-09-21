from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email

class AccountCreationForm(FlaskForm):
    '''
    Flask form used to create an account 
    '''
    username = StringField('Email Address', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min = 6)])
    submit = SubmitField('Submit')
