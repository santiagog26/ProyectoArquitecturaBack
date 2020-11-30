#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, jsonify
from flask_cors import CORS
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)

app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def hellos():
    return "Hello world"

@app.route('/get_pedidos', methods=['GET'])
def mostrar_pedidos():
	print('Hello')
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
		sql = ("select * from pedido")
		cur.execute(sql)
		row = cur.fetchall()
		lista = list()
		for i in row:
			numero_orden = i[0]
			fecha = i[1]
			cliente_documento = i[2]
			empaquetado = i[3]
			domicilio = i[4]
			vendedor = i[5]
			pedido = {'numero_orden': numero_orden, 'fecha': fecha, 'cliente_documento': cliente_documento, 'empaquetado': empaquetado, 'domicilio': domicilio, 'vendedor': vendedor}
			lista.append(pedido)
		return jsonify(results=lista)
	cnx.close()	


if __name__ == "__main__":
    app.run(host='0.0.0.0')