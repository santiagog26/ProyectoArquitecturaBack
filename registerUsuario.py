#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Nombre =data.getvalue('nombres')
Apellido =data.getvalue('apellidos')
Documento =data.getvalue('documento')
Contraseña =data.getvalue('contraseña')
Correo =data.getvalue('correo')
Telefono =data.getvalue('telefono')
Rol =data.getvalue('rol')
print(Nombre)
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
    #sql = ("insert into usuario values ('{}',SHA('{}'),'{}','{}','{}','{}')".format(Documento,Contraseña,Nombre,Apellido,Correo,Telefono))
    #cur.execute(sql)
    print('<h1> Fallo {} </h1>'.format(Documento))
    print('<h1> Fallo {} </h1>'.format(Contraseña))
    print('<h1> Fallo {} </h1>'.format(Nombre))
    print('<h1> Fallo {} </h1>'.format(Apellido))
    print('<h1> Fallo {} </h1>'.format(Correo))
    print('<h1> Fallo {} </h1>'.format(Telefono))
    cnx.commit()
cnx.close()

