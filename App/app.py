from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisjustrandom'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.sqlite3" 

db = SQLAlchemy(app)
admin =Admin(app)



#exitfrom routes import *

if __name__ == '__main__':
    app.run(debug=True)