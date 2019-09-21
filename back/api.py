from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
from pathlib import Path
import hashlib
import pandas as pd


app = Flask(__name__)
api = Api(app)
dataFolder = Path('data' / 'data.csv')
solutionsFolder = Path('data' / 'solutions.csv')


class UserId(Resource):
    def post(self, username, password):
        pd.read_csv(str(dataFolder))
        query = conn.execute("select * from employees where UserId =%d "  %int(user_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(UserId, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')
