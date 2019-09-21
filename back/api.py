from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
from pathlib import Path
import hashlib
import pandas as pd


app = Flask(__name__)

dataFolder = Path.cwd() / 'data' / 'data.csv'
solutionsFolder = Path.cwd() / 'data' / 'solutions.csv'


@app.route('/accountcreation/', methods=['POST'])
def accountCreation():
    if request.method == 'POST':

        data = request.get_json()

        if data is None:
            return json.dumps({error: "Error"})

        if request.headers.get('x-api-token') == 'jria':

            email = data['username']
            password = data['password']

            data = pd.read_csv(str(dataFolder))

            user = data.loc[data["username"] == email]

            h = hashlib.md5(password.encode())
            print(h.hexdigest())

            # If the user doesn't exist yet, put them in!
            if user.empty:

                data = data.append({'username' : email , 'password' : h.hexdigest()} , ignore_index=True)

                data.to_csv(str(dataFolder))

                return "200 - OK"

            else:
                return '405 - Method Not Allowed'

@app.route('/demographics/', methods=['POST'])
def accountCreation():
    if request.method == 'POST':
        data = request.get_json()

        if data is None:
            return json.dumps({error: "Error"})

        if request.headers.get('x-api-token') == 'jria':

            first_name = data['first_name']
            last_name = data['last_name']
            middle_name = data['middle_name']
            date_of_birth = data['date_of_birth']
            gender = data['date_of_birth']
            marital_status = data['marital_status']
            spanish_origin = data['spanish_origin']
            country_of_origin = data['country_of_origin']
            racial_group = data['racial_group']

            english_second_lang = data['english_second_lang']
            native_lang = data['native_lang']

            address = data['address']
            city = data['city']
            state = data['state']
            zip_code = data['zip_code']
            home_phone = data['home_phone']
            cell_phone = data['cell_phone']
            emergency_contact_name = data['emergency_contact_name']
            emergency_contact_num = data['emergency_contact_num']
            emergency_contact_relation = data['emergency_contact_relation']

            max_grade_completed = data['max_grade_completed']
            school_type = data['school_type']
            date_last_enrolled = data['date_last_enrolled']
            num_school_years_completed = data['num_school_years_completed']

            occupation = data['occupation']
            employer_name = data['employer_name']
            employer_address = data['employer_address']
            employment_status = data['employment_status']

            hours_per_week = data['hours_per_week']
            work_phone = data['work_phone']

            num_dependents_minor = data['num_dependents_minor']
            num_dependents_other = data['num_dependents_other']
            yearly_income = data['yearly_income']
            public_assistance = data['public_assistance']
            public_assistance_number = data['public_assistance_number']
            disability = data['disability']

            living_area = data['living_area']
            how_hear_about = data['how_hear_about']
            add_student_info = data['add_student_info']
            add_student_info2 = data['add_student_info2']

            children = data['children']
            num_children = data['num_children']
            age_children = data['age_children']
            school_type = data['school_type']
            take_care_of_kids = data['take_care_of_kids']
            immigration_status = data['immigration_status']
            government_aid = data['government_aid']

            checking_acc = data['checking_acc']
            savings_acc = data['savings_acc']
            library_card = data['library_card']

            english_classes = data['english_classes']
            english_class_details = data['english_class_details']

            work = data['work']
            work_benefits = data['work_benefits']

            house_or_rent = data['house_or_rent']

            smartphone = data['smartphone']
            tablet = data['tablet']
            computer = data['computers']
            internet = data['internet']
            internet_access = data['internet_access']
            internet_access_elsewhere = data['internet_access_elsewhere']

            why_learn_english = data['why_learn_english']


            data = pd.read_csv(str(dataFolder))
            user = data.loc[data["username"] == email]
            index = data.index[[data["username"] == email]


            if not user.empty:
                user.loc[]

                return "200 - OK"

            else:
                return '405 - Method Not Allowed'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
