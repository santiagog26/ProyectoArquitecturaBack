#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Documento =data.getvalue('documentodo')#obtiene informacion del formulario
Numero_pedido =data.getvalue('numero_pedido')#obtiene informacion del formulario
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
    sql = ("update pedido set domicilio=(select rol from domiciliario where documento_domiciliario='{}') where numero_orden='{}';".format(Documento,Numero_pedido))#codigo de mysql para actualizar un pedido
    cur.execute(sql)
    print('<script>alert("pedido entregado ")</script>')#alerta de que se actualizo el pedido
    print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')#me devuelve al menu.html
    cnx.commit()
cnx.close()