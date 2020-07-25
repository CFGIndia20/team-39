from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt import JWT,jwt_required
import sqlite3

from security import authenticate, identity
from user import User

app = Flask(__name__)
CORS(app)

app.secret_key = 'ayesha'

jwt = JWT(app, authenticate,identity)


users=[]
@jwt_required
@app.route('/signin',methods=['POST'])
def signin():
    request_data = request.get_json()
    user_signin = {
        'user_name': request_data['name_value'],
        'password': request_data['pass_value']
    }
    users.append(user_signin)
    return user_signin

@app.route('/signup', methods=['POST'])
def signup():

    request_data = request.get_json()
    if User.find_by_username(request_data['name_value']):
        return {'message': 'user of that username already exists'}, 400

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "INSERT INTO users VALUES(NULL,?,?,?)"
    

    cursor.execute(query, (request_data['name_value'], request_data['pass_value'], request_data['email_value']))

    connection.commit()
    connection.close()

    new_user = {
        'user_name': request_data['name_value'],
        'password': request_data['pass_value'],
        'email': request_data['email_value']
    }
    
    users.append(new_user)
    return new_user

app.run(port=5000)
    

