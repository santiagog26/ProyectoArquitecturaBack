#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi
from jinja2 import Template
data = cgi.FieldStorage()
Nombrep =data.getvalue('nombrep')
Descripcionp =data.getvalue('descripcionp')
preciop =int(data.getvalue('preciop'))
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
    sql = ("insert into producto (nombre_producto, descripcion, precio) values ('{}','{}','{}')".format(Nombrep,Descripcionp,preciop))
    cur.execute(sql)
    sql = ("select id_producto from producto where nombre_producto='{}'".format(Nombrep))
    cur.execute(sql)
    id=cur.fetchall()
    #print('<script>alert("Registro exitoso de un Producto ")</script>')
    #print('<script> location.href="/ProyectoArquitectura/menu.html";</script>')
    with open('/ProyectoArquitectura/menu.html') as f:
        doc = f.read()
        template = Template(doc)
        page = template.render(idp=id)
        print(page)
    cnx.commit()
cnx.close()