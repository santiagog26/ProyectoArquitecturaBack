#!/usr/bin/python3
#from jinja2 import Template
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Nombrep =data.getvalue('nombrep')#obtiene informacion del formulario
Descripcionp =data.getvalue('descripcionp')#obtiene informacion del formulario
preciop =int(data.getvalue('preciop'))#obtiene informacion del formulario
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
    sql = ("insert into producto (nombre_producto, descripcion, precio) values ('{}','{}','{}')".format(Nombrep,Descripcionp,preciop))#codigo de mysql para insertar un producto
    cur.execute(sql)
    print('<script>alert("Registro exitoso de un Producto ")</script>')#alerta de que el registro fue exitoso 
    print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')#me devuelve al menu.html
    cnx.commit()
cnx.close()
