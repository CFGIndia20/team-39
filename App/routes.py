from App import db, app
from flask import render_template,request, url_for
from flask_login import login_user, current_user, logout_user, login_required
import secrets

@app.route("/")
@app.route("/home")
def home():
    render_template("home.html")

@app.route('/sysadmin')
def Admin():
    return render_template('admin_home.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')
