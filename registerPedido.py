#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Fecha =data.getvalue('fecha')
Documentocl =data.getvalue('documentocl')
Documentoven =data.getvalue('documentoven')

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
    sql = ("insert into pedido (fecha,cliente_documento,vendedor) values ('{}','{}',(select rol from vendedor where documento_vendedor='{}'));".format(Fecha,Documentocl,Documentoven))
    cur.execute(sql)
    print('<script>alert("Registro exitoso de un Cliente ")</script>')
    print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')
    cnx.commit()
cnx.close()