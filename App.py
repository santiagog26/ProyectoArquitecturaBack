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

@app.route('/get_usuarios', methods=['GET'])
def mostrar_usuarios():
    try:
        cnx = mysql.connector.connect(
            user='sebastian', password = 'Holasebas99.', database='proyecto', host='127.0.0.1')
    except mysql.connector.Error as err:
    	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
    	cur = cnx.cursor()
		sql = ("select* from usuario")
		cur.execute(sql)
		row = cur.fetchall()
		lista = list()
		for i in row:
			documento = i[0]
			contrasena = i[1]
			nombre = i[2]
			apellido = i[3]
			correo = i[4]
			telefono = i[5]
			persona = {'Documento': documento,
			'Contraseña': contrasena,
            'Nombre': nombre,
            'Apellido': apellido,
            'Correo': correo,
            'Telefono': telefono}
            lista.append(persona)
        return jsonify(results=lista)
    cnx.close()	


@app.route('/productosMO', methods=['PUT'])
def modificar_productos():
    return "Modificando producto uwu"


@app.route('/productosB', methods=['DELETE'])
def borrar_productos():
    return "borrando producto unu"


@app.route('/productosC', methods=['POST'])
def crear_productos():
    return "creando producto ewe"


if __name__ == "__main__":
    app.run(host='0.0.0.0')