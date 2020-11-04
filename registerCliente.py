#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Nombre =data.getvalue('nombresc')#obtiene informacion del formulario 
Apellido =data.getvalue('apellidosc')#obtiene informacion del formulario 
Documento =data.getvalue('documentoc')#obtiene informacion del formulario 
Correo =data.getvalue('correoc')#obtiene informacion del formulario 
Telefono =data.getvalue('telefonoc')#obtiene informacion del formulario 
#conexion a base de datos
try:
  cnx = mysql.connector.connect(user='sebastian', password = 'Holasebas99.', database='proyecto', host='127.0.0.1')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with you")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cur = cnx.cursor()
    print('Content-Type: text/html')
    print('')
    sql = ("insert into cliente values ('{}','{}','{}','{}','{}')".format(Documento,Nombre,Apellido,Correo,Telefono))#codigo de mysql para insertar un Cliente
    cur.execute(sql)
    print('<script>alert("Registro exitoso de un Cliente ")</script>')#alerta de que el registro fue exitoso 
    print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')#me devuelve al menu.html
    cnx.commit()
cnx.close()