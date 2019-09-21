from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, validators
from wtforms.validators import DataRequired, Email, Length, input_required

class AccountCreationForm(FlaskForm):
    '''
    Flask form used to create an account
    '''
    username = StringField('Email Address', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired(), Length(min = 6, message = "Password should be at least 6 characters.")])
    submit = SubmitField('Submit')

class DemographicForm(FlaskForm):
    first_name = StringField(u'First Name', validators=[validators.input_required()])
    last_name  = StringField(u'Last Name', validators=[validators.input_required()])
    middle_name  = StringField(u'Middle Name', validators=[validators.optional()])
    date_of_birth = StringField(u'Date of Birth', validators=[validators.input_required()])
    gender = BooleanField() #gender
    marital_status = SelectField(u'Programming Language', choices=[('Single', 'Single'),
    ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widow', 'Widow')])
    spanish_origin = BooleanField();  #Are you hispanic or latino?
    country_of_origin = StringField(u'Country of origin', validators=[validators.optional()])
    racial_group = SelectField(u'Are you from one or more of the following racial groups?',
    choices=[('American Indian or Alaska Native', 'American Indian or Alaska Native'),
    ('Asian', 'Asian'), ('Black or African American', 'Black or African American'),
    ('Native Hawaiian or Pacific Islander', 'Native Hawaiian or Pacific Islander')])
