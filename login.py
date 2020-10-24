#!/usr/bin/python3
import hashlib
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Usuario =data.getvalue('Usuario')
Contra =data.getvalue('Contra')
try:
  cnx = mysql.connector.connect(user='sebastian', password = 'Holasebas99.', database='arqui', host='127.0.0.1')
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

    sql = ("select* from usuario where Usuario = '{}' ".format(Usuario))
    cur.execute(sql)
    usuariob=cur.fetchall()
    if usuariob:
     for i in usuariob:
      usuario=i[2]
      contra=i[0]
    else:
     print('<h1> Fallo </h1>')

    if 	Contra == contra and Usuario == usuario:
     print('<script> location.href="/ProyectoArquitectura/Login.html";</script>')
    else:
     print('<h1> Fallo </h1>')
    cnx.commit()
cnx.close()

