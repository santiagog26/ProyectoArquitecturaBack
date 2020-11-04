#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from jinja2 import Template
import cgi

def infTabla(numero_orden,fecha,cliente,empacador,vendedor, domiciliario):
    with open('/var/www/html/ProyectoArquitectura/menu.html') as f:
        doc = f.read()
        template = Template(doc)
        page = template.render(numeroOrden=numero_orden, fecha=fecha, cliente=cliente, empacador=empacador, vendedor=vendedor, domiciliario=domiciliario)
        print(page)
    

data = cgi.FieldStorage()
Documento =data.getvalue('documento')
Contra =data.getvalue('Contra')
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
    sql = ("select * from pedido")
    cur.execute(sql)
    pedido=cur.fetchall()
    for i in pedido:
        numero_orden=i[0]
        fecha=i[1]
        cliente=i[2]
        empacador=i[3]
        vendedor=i[4]
        domiciliario=i[5]
        infTabla(numero_orden,fecha,cliente,empacador,vendedor, domiciliario)
    cnx.commit()
cnx.close()

