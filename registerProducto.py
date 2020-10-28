#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
data = cgi.FieldStorage()
Idp =data.getvalue('idp')
Nombrep =data.getvalue('nombrep')
Descripcionp =data.getvalue('descripcionp')
preciop =data.getvalue('preciop')
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
    sql = ("insert into producto values ('{}','{}','{}','{}')".format(Idp,Nombrep,Descripcionp,preciop))
    cur.execute(sql)
    print('<script>alert("Registro exitoso de un Producto ")</script>')
    print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')
    cnx.commit()
cnx.close()