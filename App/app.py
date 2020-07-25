import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.sqlite3"

db = SQLAlchemy(app)


#exitfrom routes import *

if __name__ == '__main__':
    app.run(debug=True)
