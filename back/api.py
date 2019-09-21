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

            # If the user doesn't exist yet, put them in!
            if user == None:
                userdf = pd.DataFrame({"username":username,
                                        "password": h.hexdigest()})
                # Append data to bottom of database
                data.append(userdf)
                return jsonify("200 - OK")

            else:
                return jsonify('405 - Method Not Allowed')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
