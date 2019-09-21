from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, SelectMultipleField, validators
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
    home_phone = StringField('Home Phone', validators=[validators.optional()])
    cell_phone = StringField('Cell Phone', validators=[validators.optional()])
    emergency_contact_name = StringField('Emergency contact name', validators=[validators.input_required()])
    emergency_contact_num = StringField('Emergency contact phone number', validators=[validators.input_required()])
    emergency_contact_relation = StringField('Emergency contact relationship', validators=[validators.input_required()])

    #education
    max_grade_completed = StringField('Maximum grade of education completed', validators=[validators.input_required()])
    school_type = BooleanField() #us based schooling or non-us based schooling
    date_last_enrolled = StringField('Month/Year when last enrolled', validators=[validators.input_required()])
    num_school_years_completed = SelectField(u'Number of school years completed',
    choices=[('Grade 1', 'Grade 1'), ('Grade 2', 'Grade 2'), ('Grade 3', 'Grade 3'),
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
    public_assistance_number = StringField('If yes, public assistance number', validators=[validators.optional()])
    disability = SelectField(u'Do you have a disability?', choices=[('Not Disabled','Not Disabled'), ('Physical Impairment', 'Physical Impairment'),('Mental Impairment', 'Mental Impairment'), ('Learning Impairment', 'Learning Impairment'), ('Multiple disabilities', 'Multiple disabilities')])

    living_area = SelectField(u'What area do you live in?', choices=[('Rural Area', 'Rural Area'), ('Urban Area', 'Urban Area (with high unemployment)'), ('Neither', 'Neither')])
    how_hear_about = SelectField(u'How did you hear about us?', choices=[('Friend or Relative', 'Friend or Relative'), ('TV, radio, newspaper', 'TV, radio, newspaper'), ('Flyer', 'Flyer'), ('Other', 'Other')])
    add_student_info = SelectMultipleField(u'Additional Student information', choices=[('Low income', 'Low income'), ('Displaced Homemaker', 'Displaced Homemaker'), ('Single Parent', 'Single Parent'), ('Dislocated worker', 'Dislocated worker'), ('Veteran', 'Veteran')])
    add_student_info2 = SelectMultipleField(u'Please check all that apply', choices=[('Participant in a work based learner project', 'Participant in a work based learner project'), ('Participant in a Family Literacy Program', 'Participant in a Family Literacy Program'),
    ('Participant in a WorkPlace Literacy program', 'Participant in a WorkPlace Literacy program'), ('Participant in a Volunteer Literacy program','Participant in a Volunteer Literacy program'), ('In Program for the homeless', 'In Program for the homeless'),
    ('In a correctional facility', 'In a correctional facility'), ('In a community correctional program', 'In a community correctional program'), ('In other institutional setting', 'In other institutional setting')])

    children = BooleanField()
    num_children = StringField(u'How many children do you have?', validators=[validators.optional()])
    age_children = StringField(u'How old are they?', validators=[validators.optional()])
    school_type = SelectField(u'What type of school do they attend?', choices=[('Public', 'Public'), ('Private', 'Private'), ('Charter', 'Charter'), ('None', 'None')])
    take_care_of_kids = BooleanField() #Do you take good care of your kids?
    immigration_status = SelectField(u'Immigration status', choices=[('Citizen', 'Citizen'), ('Resident', 'Resident'), ('Visitor', 'Visitor'), ('None', 'None')])
    government_aid = SelectMultipleField(u'If you recieve aid from the government, which ones are they?', choices=[('TANF', 'TANF'), ('Tax Credit', 'Tax Credit'), ('SNAP/Link', 'SNAP/Link'), ('WIC', 'WIC'), ('Medical Card', 'Medical Card'), ('Medicare', 'Medicare'), ('others', 'others')])

    checking_acc = BooleanField() #Do you have a checkign account?
    savings_acc = BooleanField() #Do you have a savings account?
    library_card = BooleanField() #Do you have a library card?

    english_classes = BooleanField() #Have you taken english language classes?
    english_class_details = StringField(u'Where and what year?', validators=[validators.optional()])

    work = StringField(u'If you work, what is your job?', validators=[validators.optional()])
    work_benefits = SelectMultipleField(u'If you work, whar benefits do you recieve?', choices=[('Medical Insurance', 'Medical Insurance'), ('Vacations/Holidays/Sickeness/Maternity/Personal', 'Vacations/Holidays/Sickeness/Maternity/Personal'), ('Flexiible hours', 'Flexible hours'), ('Retirement plan', 'Retirement plan'), ('Other', 'Other')])

    house_or_rent = BooleanField() #Do you own a house or pay rent?

    smartphone = BooleanField() #Do you have a smartphone
    tablet = BooleanField() #Do you have a tablet
    computer = BooleanField() #Do you have a computer
    internet = BooleanField() #Have you ever used the internet?
    internet_access = BooleanField() #Do you have internet access at home?
    internet_access_elsewhere = BooleanField() #Do you have internet access elsewhere?

    why_learn_english = SelectMultipleField('Why do you want to learn english?', choices=[('GED', 'GED'), ('Job', 'Job'), ('Citizenship', 'Citizenship'), ('To get an education', 'To get an education'), ('Move forward at work', 'Move forward at work'), ('Help kids at school', 'Help kids at school')])
    submit = SubmitField('Submit')

class CareerInterest(FlaskForm):
    career_interest = SelectField('Select one field that is a career cluster you are interested in pursuing', choices= [
    ('Agriculture Food & Natural Resources', 'Agriculture Food & Natural Resources'),
    ('Architecture & Construction', 'Architecture & Construction'),
    ('Arts, A/V Technology & Communication', 'Arts, A/V Technology & Communication'),
    ('Business Management & Administration', 'Business Management & Administration'),
    ('Education & Training', 'Education & Training'),
    ('Finance', 'Finance'),
    ('Government & Public Administration', 'Government & Public Administration'),
    ('Health Sciences', 'Health Sciences'),
    ('Hospitality and Tourism', 'Hospitality & Tourism'),
    ('Human Services', 'Human Services'),
    ('Information Technology', 'Information Technology'),
    ('Law, Public Safety, Corrections & Security', 'Law, Public Safety, Corrections & Security'),
    ('Manufacturing', 'Manufacturing'),
    ('Marketing', 'Marketing'),
    ('Science, Technology, Engineering & Mathematics', 'Science, Technology, Engineering & Mathematics'),
    ('Transportation, Distribution & Logistics','Transportation, Distribution & Logistics')
    ])
