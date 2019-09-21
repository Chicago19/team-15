import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, SelectMultipleField, TextField
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



orientation = ""

class ScheduleOrientation(FlaskForm):
    start_date_fall = datetime.datetime(2019, 8, 26)
    start_date_spring = datetime.datetime(2020, 1, 1)
    start_date_summer = datetime.datetime(2020, 5, 10)
    today = datetime.datetime.now()
    possible_dates = []
    while (today <= start_date_fall + datetime.timedelta(days=70)):
        possible_dates.append((str(today), str(today)))
        today += datetime.timedelta(days = 1)
    orientation = SelectMultipleField('Select the dates you are available for orientation', choices=possible_dates) #to_display
    submit = SubmitField('submit')

class printUpcomingDates(FlaskForm):
    start_date_fall = datetime.datetime(2019, 8, 26)
    start_date_spring = datetime.datetime(2020, 1, 1)
    start_date_summer = datetime.datetime(2020, 5, 10)
    today = datetime.datetime.now()
    #print out upcoming class dates
    #can change const 7 ddepending if class is weekly, biweekly, daily, etc
    upcoming_class_dates = []
    class_date = start_date_fall
    while (class_date <= start_date_spring):
        if class_date > today:
             upcoming_class_dates.append(class_date)
        class_date += datetime.timedelta(days = 7)

    orientation_date = TextField('Upcoming orientation date: ' + orientation)
    output_classes = TextField('Upcoming classes are on dates: ' + str(upcoming_class_dates))
