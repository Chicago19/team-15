from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length

class AccountCreationForm(FlaskForm):
    '''
    Flask form used to create an account
    '''
    username = StringField('Email Address', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min = 6, message = "Password should be at least 6 characters.")])
    submit = SubmitField('Submit')

class DashboardForm(FlaskForm):
    grades = SubmitField('Grades')
    calendar = SubmitField('Calendar')
    editprofile = SubmitField('Edit Profile')
    attendance = SubmitField('Attendance')
    
