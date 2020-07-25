from flask import Flask
from flask_sqlalchemy import sqlalchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisjustrandom'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'

from routes import *

if __name__ == '__main__':
    app.run(debug=True)