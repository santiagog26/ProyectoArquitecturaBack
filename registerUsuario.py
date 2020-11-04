#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Nombre =data.getvalue('nombres')#obtiene informacion del formulario 
Apellido =data.getvalue('apellidos')#obtiene informacion del formulario 
Documento =data.getvalue('documento')#obtiene informacion del formulario 
Contraseña =data.getvalue('contraseña')#obtiene informacion del formulario 
Correo =data.getvalue('correo')#obtiene informacion del formulario 
Telefono =data.getvalue('telefono')#obtiene informacion del formulario 
Rol =int(data.getvalue('rol'))#obtiene informacion del formulario 
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
    sql = ("insert into usuario values ('{}',SHA('{}'),'{}','{}','{}','{}')".format(Documento,Contraseña,Nombre,Apellido,Correo,Telefono))#codigo de mysql para insertar un Usuario 
    cur.execute(sql)
    #verifica el rol del usuario 
    if Rol == 1: 
      sql = ("insert into vendedor (documento_vendedor) values ('{}')".format(Documento))#codigo de mysql para insertar el documento de un vendedor  
      cur.execute(sql)
      print('<script>alert("Registro exitoso de un vendedor ")</script>')#alerta de que el registro fue exitoso 
      print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')#me devuelve al menu.html
    if Rol == 2:
      sql = ("insert into domiciliario (documento_domiciliario) values ('{}')".format(Documento))#codigo de mysql para insertar el documento de un domiciliario 
      cur.execute(sql)
      print('<script>alert("Registro exitoso de un domiciliario ")</script>')#alerta de que el registro fue exitoso 
      print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')#me devuelve al menu.html
    if Rol == 3:
      sql = ("insert into empacador (documento_empacador) values ('{}')".format(Documento))#codigo de mysql para insertar el documento de un empacador  
      cur.execute(sql)
      print('<script>alert("Registro exitoso de un enpacador ")</script>')#alerta de que el registro fue exitoso 
      print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')#me devuelve al menu.html
    cnx.commit()
cnx.close()


