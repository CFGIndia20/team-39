from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/donor')
def donor():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    data1 = []
    query = "SELECT * FROM table1"
    for row in cursor.execute(query):
        data1.append(row)
    
    data2 = []
    query = "SELECT * FROM table2"
    for row in cursor.execute(query):
        data2.append(row)
    
    data3 = []
    query = "SELECT * FROM table3"
    for row in cursor.execute(query):
        data3.append(row)
    
    connection.close()

    return{'result1':data1,'result2':data2,'result3':data3}


app.run(port = 4001)