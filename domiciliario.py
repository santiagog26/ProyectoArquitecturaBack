#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Documento =data.getvalue('documentodo')
Numero_pedido =data.getvalue('numero_pedido')

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
    sql = ("update pedido set domicilio=(select rol from domiciliario where documento_domiciliario='{}') where numero_orden='{}';".format(Documento,Numero_pedido))
    cur.execute(sql)
    print('<script>alert("pedido empacado y actualizado ")</script>')
    print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')
    cnx.commit()
cnx.close()