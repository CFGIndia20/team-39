from App import db, app
from flask import render_template,request, url_for

@app.route('/admin')
def Admin():
    return render_template('admin.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')