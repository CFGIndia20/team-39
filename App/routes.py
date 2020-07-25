from app import app,db
from flask import render_template,request

@app.route('/admin')
def Admin():
    return render_template('admin.py')

