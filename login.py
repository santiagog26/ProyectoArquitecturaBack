#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Usuario =data.getvalue('Usuario')
Nombre =data.getvalue('Nombre')
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

    sql = ("select* from usuario where Usuario = '{}' and Contraseña = SHA('{}')  ".format(Usuario,Nombre))
    cur.execute(sql)
    usuariob=cur.fetchall()
    if usuariob:
      print('<script> location.href="/ProyectoArquitectura/Login.html";</script>')
    else:
     print('<h1> Fallo </h1>')
    cnx.commit()
cnx.close()

