from flask import Flask, render_template, request, redirect
from config import Config
import threading, webbrowser
from forms import AccountCreationForm, DemographicForm
import requests
import json



app = Flask(__name__)
app.config.from_object(Config)

@app.route('/home/', methods=['GET','POST'])
def renderHome():
    '''
    Renders a viewable web application on your port:
    http://127.0.0.1:5000/home
    '''

    return (render_template('home.html') )

@app.route('/accountcreation/', methods=['GET', 'POST'])
def renderAccountCreation():
    if request.method == "GET":
        form = AccountCreationForm()
        return (render_template('accountcreation.html', form = form))

    elif request.method == "POST":
        username = request.form['username'].strip()
        password = request.form['password']

        url = "http://0.0.0.0:8080/accountcreation/"

        # Yes, the x-api-token is weird. No, I don't know why I picked it.
        headers = {
            'content-type': 'application/json',
            'x-api-token': 'jria'
        }

        payload = {
                'username': username,
                'password': password
        }

        requests.post(url, headers=headers, data=json.dumps(payload))

        return(redirect("http://127.0.0.1:5000/demographics/"))

@app.route('/demographics/', methods=["GET", "POST"])
def renderDemographicForm():
    if request.method == "GET":
        form = DemographicForm()
        return(render_template('demographic.html', form = form))

    elif request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        middle_name = request.form['middle_name']
        date_of_birth = request.form['date_of_birth']
        gender = request.form['date_of_birth']
        marital_status = request.form['marital_status']
        spanish_origin = request.form['spanish_origin']
        country_of_origin = request.form['country_of_origin']
        racial_group = request.form['racial_group']

        english_second_lang = request.form['english_second_lang']
        native_lang = request.form['native_lang']

        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        home_phone = request.form['home_phone']
        cell_phone = request.form['cell_phone']
        emergency_contact_name = request.form['emergency_contact_name']
        emergency_contact_num = request.form['emergency_contact_num']
        emergency_contact_relation = request.form['emergency_contact_relation']

        max_grade_completed = request.form['max_grade_completed']
        school_type = request.form['school_type']
        date_last_enrolled = request.form['date_last_enrolled']
        num_school_years_completed = request.form['num_school_years_completed']

        occupation = request.form['occupation']
        employer_name = request.form['employer_name']
        employer_address = request.form['employer_address']



        return(redirect("http://127.0.0.1:5000/careerinterests/"))

@app.route('/careerinterests/', methods=["GET", "POST"])
def renderCareerInterestForm():
    if request.method == "GET":
        form = CareerInterest()
        return(render_template('careerinterest.html', form = form))

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/home'
    app.run()

 # Pizarron
