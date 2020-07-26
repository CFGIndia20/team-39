import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.sqlite3"

db = SQLAlchemy(app)
admin = Admin(app)

@app.route("/dashboard")
def dashboard():
    return render_template('../admin_temp/dashboard.html')
#exitfrom routes import *

if __name__ == '__main__':
    app.run(debug=True)
