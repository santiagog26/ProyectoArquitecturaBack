#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
from flask import Flask, render_template
data = cgi.FieldStorage()
Documento =data.getvalue('documento')
Contra =data.getvalue('Contra')
try:
  cnx = mysql.connector.connect(user='sebastian', password = 'Holasebas99.', database='proyecto', host='127.0.0.1')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cur = cnx.cursor()
    print('Content-Type: text/html')
    print('')

    sql = ("select * from pedido")
    cur.execute(sql)
    pedido=cur.fetchall()
    cnx.commit()
    app = Flask(__name__)
cnx.close()


@app.route("/")
def table():
  return render_template("/ProyectoArquitectura/menu.html",data=pedido)
