#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Documento =data.getvalue('documento')#obtiene informacion del formulario
Contra =data.getvalue('Contra')#obtiene informacion del formulario
#conexion a base de datos
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

    sql = ("select * from usuario where documento = '{}' and contraseña = SHA('{}')  ".format(Documento,Contra))#codigo de mysql para comprobar si un usuario existe 
    cur.execute(sql)
    usuariob=cur.fetchall()
    if usuariob:
      print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')#me manda menu.html si el usuario existe 
    else:
     print('<h1> Fallo </h1>')#mensaje de error si no existe el usuario 
    cnx.commit()
cnx.close()

