#!/usr/bin/python3
from flask import Flask, render_template
from mysql.connector import errorcode
import mysql.connector

app = Flask(__name__)

try:
  cnx = mysql.connector.connect(user='sebastian', password = 'Holasebas99.', database='proyecto', host='127.0.0.1')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with you")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

@app.route('/')
def Index():
	return 'Hello world'

@app.route('/add_usuario')
def add_usuario():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)