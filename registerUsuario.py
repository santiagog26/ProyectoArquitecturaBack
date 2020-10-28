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
Rol =int(data.getvalue('rol'))
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
    sql = ("insert into usuario values ('{}',SHA('{}'),'{}','{}','{}','{}')".format(Documento,Contraseña,Nombre,Apellido,Correo,Telefono))
    cur.execute(sql)
    if Rol == 1:
      sql = ("insert into vendedor (documento_vendedor) values ('{}')".format(Documento))
      cur.execute(sql)
      print('<script>alert("Registro exitoso de un vendedor ")</script>')
    if Rol == 2:
      sql = ("insert into domiciliario (documento_domiciliario) values ('{}')".format(Documento))
      cur.execute(sql)
      print('<script>alert("Registro exitoso de un domiciliario ")</script>')
    if Rol == 3:
      sql = ("insert into empacador (documento_empacador) values ('{}')".format(Documento))
      cur.execute(sql)
      print('<script>alert("Registro exitoso de un enpacador ")</script>')
    cnx.commit()
cnx.close()


