from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length, input_required, optional

class AccountCreationForm(FlaskForm):
    '''
    Flask form used to create an account
    '''
    username = StringField('Email Address', validators=[validators.input_required(), Email()])
    password = StringField('Password', validators=[validators.input_required(), Length(min = 6, message = "Password should be at least 6 characters.")])
    submit = SubmitField('Submit')


class DemographicForm(FlaskForm):
    first_name = StringField(u'First Name:', validators=[input_required()])
    last_name  = StringField(u'Last Name:', validators=[input_required()])
    middle_name  = StringField(u'Middle Name:', validators=[optional()])
    date_of_birth = StringField(u'Date of Birth:', validators=[input_required()])
    gender = BooleanField() #gender
    marital_status = SelectField(u'Marital Status:', choices=[('Single', 'Single'),
    ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widow', 'Widow')])
    spanish_origin = BooleanField();  #Are you hispanic or latino?
    country_of_origin = StringField(u'Country of origin:', validators=[optional()])
    racial_group = SelectField(u'Are you from one or more of the following racial groups?',
    choices=[('American Indian or Alaska Native', 'American Indian or Alaska Native'),
    ('Asian', 'Asian'), ('Black or African American', 'Black or African American'),
    ('Native Hawaiian or Pacific Islander', 'Native Hawaiian or Pacific Islander'),
    ('White', 'White')])

    english_second_lang = BooleanField()
    native_lang = StringField(u'If yes, record native language', validators=[validators.optional()])

    #contact info
    address = StringField('Address', validators=[validators.input_required()])
    city = StringField('City', validators=[validators.input_required()])
    state = StringField('State', validators=[validators.input_required()])
    zip_code = StringField('Zip Code', validators=[validators.input_required()])
    home_phone = StringField('Home Phone', validators=[validators.input_required()])
    cell_phone = StringField('Cell Phone', validators=[validators.input_required()])
    emergency_contact_name = StringField('Emergency contact name', validators=[validators.input_required()])
    emergency_contact_num = StringField('Emergency contact phone number', validators=[validators.input_required()])
    emergency_contact_relation = StringField('Emergency contact relationship', validators=[validators.input_required()])

    #education
    max_grade_completed = StringField('Maximum grade of education completed', validators=[validators.input_required()])
    school_type = BooleanField() #us based schooling or non-us based schooling
    date_last_enrolled = StringField('Month/Year when last enrolled', validators=[validators.input_required()])
    num_school_years_completed = SelectField(u'Number of school years completed',
    choices=[('Grade 1', 'Grade 1'), ('Grade 2', 'Grade 2'), ('Grade 3', 'Grade 3')
    ('Grade 4', 'Grade 4'), ('Grade 5', 'Grade 5'), ('Grade 6', 'Grade 6'), ('Grade 7', 'Grade 7'),
    ('Grade 8', 'Grade 8'), ('Grade 9', 'Grade 9'), ('Grade 10', 'Grade 10'), ('Grade 11', 'Grade 11'),
    ('Grade 12', 'Grade 12'), ('High School Diploma', 'High School Diploma'), ('GED', 'GED'),
    ('Some college', 'Some college'), ('College Degree', 'College Degreee')])

    #employment
    occupation = StringField('If employed, what is your occupation?', validators=[validators.optional()])
    employer_name = StringField('Employer name', validators=[validators.optional()])
    employer_address = StringField('Employer address', validators=[validators.optional()])
    employment_status = SelectField('Employment status', choices=[('Not in labor force', 'Not in labor force'),
    ('Employed part-time', 'Employed part-time'), ('Unemployed', 'Unemployed'), ('Employed full time', 'Employed full time')])

    hours_per_week = StringField('If Employed, hours per week', validators=[validators.optional()])
    work_phone = StringField('Work Phone#', validators=[validators.optional()])

    #Student status
    num_dependents_minor = StringField('Number of Dependents-minor children', validators=[validators.optional()])
    num_dependents_other = StringField('Number of Dependents-other', validators=[validators.optional()])
    yearly_income = num_dependents_minor = StringField('Yearly household income', validators=[validators.input_required()])
    public_assistance = BooleanField() #do you recieve public assistance?
    public_assistance_number = StringField('If yes, public assistance number', validators=[validators.optional()]
    disability = SelectField(u'Do you have a disability?', choices=[('Not Disabled','Not Disabled'), ('Physical Impairment', 'Physical Impairment'),
    ('Mental Impairment', 'Mental Impairment'), ('Learning Impairment', 'Learning Impairment'), ('Multiple disabilities', 'Multiple disabilities')])
    
