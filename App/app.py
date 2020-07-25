from flask import Flask
from flask_sqlalchemy import sqlalchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisjustrandom'

from routes import *

if __name__ == '__main__':
    app.run(debug=True)