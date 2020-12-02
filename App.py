#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)

app.config.from_object(__name__)

CORS(app)
@app.route('/')
def hellos():
    return "Hello world"

try:
	cnx = mysql.connector.connect(user='sebastian', password = 'Holasebas99.', database='proyecto', host='127.0.0.1')
	
	CORS(app)
	@app.route('/get_pedidos', methods=['GET'])
	def mostrar_pedidos():
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
			cnx.commit()
			cur.close()
		return jsonify(results=lista)

	CORS(app)
	@app.route('/get_usuarios', methods=['GET'])
	def mostrar_usuario():
		cur = cnx.cursor()
		sql = ("select * from usuario")
		cur.execute(sql)
		row = cur.fetchall()
		lista = list()
		for i in row:
			documento = i[0]
			contraseña = i[1]
			nombre = i[2]
			apellido = i[3]
			correo = i[4]
			telefono = i[5]
			usuario = {'documento': documento, 'contraseña': contraseña, 'nombre': nombre, 'apellido': apellido, 'correo': correo, 'telefono': telefono}
			lista.append(usuario)
			cnx.commit()
			cur.close()
		return jsonify(results=lista)

	CORS(app)
	@app.route('/get_producto', methods=['GET'])
	def mostrar_producto():
		cur = cnx.cursor()
		sql = ("select * from producto")
		cur.execute(sql)
		row = cur.fetchall()
		lista = list()
		for i in row:
			id_producto = i[0]
			nombre_producto = i[1]
			descripcion = i[2]
			precio = i[3]
			producto = {'id_producto': id_producto, 'nombre_producto': nombre_producto, 'descripcion': descripcion, 'precio': precio}
			lista.append(producto)
			cnx.commit()
			cur.close()
		return jsonify(results=lista)

	CORS(app)
	@app.route('/get_clientes', methods=['GET'])
	def mostrar_cliente():
		cur = cnx.cursor()
		sql = ("select * from cliente")
		cur.execute(sql)
		row = cur.fetchall()
		lista = list()
		for i in row:
			documento_cliente = i[0]
			nombre = i[1]
			apellido = i[2]
			correo = i[3]
			telefono = i[4]
			cliente = {'documento_cliente': documento_cliente, 'nombre': nombre, 'apellido': apellido, 'correo': correo, 'telefono': telefono}
			lista.append(cliente)
			cnx.commit()
			cur.close()
		return jsonify(results=lista)

	CORS(app)
	@app.route('/get_pedidos_cliente/<cliente_documento>', methods=['GET'])
	def mostrar_pedido_cli(cliente_documento):
		cur = cnx.cursor()
		sql = ("select * from pedido where cliente_documento = {}".format(cliente_documento))
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
			cnx.commit()
			cur.close()
		return jsonify(results=lista)

	CORS(app)
	@app.route('/get_comentarios_cliente', methods=['GET'])
	def mostrar_comentarios_cli():
		cur = cnx.cursor()
		data = request.get_json(force=True)
		documento_cliente = data.get('documento_cliente')
		sql = ("select * from comentarios where documento_cliente = {}".format(documento_cliente))
		cur.execute(sql)
		row = cur.fetchall()
		lista = list()
		for i in row:
			documento_usuario = i[0]
			documento_cliente = i[1]
			comentario = i[2]
			comentarios_cli = {'documento_usuario': documento_usuario, 'documento_cliente': documento_cliente, 'comentario': comentario}
			lista.append(comentarios_cli)
			cnx.commit()
			cur.close()
		return jsonify(results=lista)

	CORS(app)
	@app.route('/add_comentarios', methods=['POST'])
	def add_com():
		cur = cnx.cursor()
		data = request.get_json(force=True)
		documento_usuario = data.get('documento_usuario')
		documento_cliente = data.get('documento_cliente')
		comentario = data.get('comentario')
		cur.execute('insert into comentarios (documento_usuario,documento_cliente,comentario) values (%s,%s,%s)',(documento_usuario,documento_cliente,comentario))
		cnx.commit()
		cur.close()
		return 'Agregado';

	CORS(app)
	@app.route('/editar_usuarios', methods=['PUT'])
	def edit_user():
		cur = cnx.cursor(buffered=True)
		data = request.get_json(force=True)
		documento = data.get('documento')
		contraseña = data.get('contraseña')
		nombre = data.get('nombre')
		apellido = data.get('apellido')
		correo = data.get('correo')
		telefono = data.get('telefono')
		cur.execute('update usuario set contraseña = %s, nombre = %s, apellido = %s, correo = %s, telefono = %s where documento = %s', (contraseña,nombre,apellido,correo,telefono,documento))
		cnx.commit()
		cur.close()
		return 'Editado';

	CORS(app)
	@app.route('/editar_cliente', methods=['PUT'])
	def edit_cli():
		cur = cnx.cursor(buffered=True)
		data = request.get_json(force=True)
		documento_cliente = data.get('documento_cliente')
		nombre = data.get('nombre')
		apellido = data.get('apellido')
		correo = data.get('correo')
		telefono = data.get('telefono')
		cur.execute('update cliente set nombre = %s, apellido = %s, correo = %s, telefono = %s where documento_cliente = %s', (nombre,apellido,correo,telefono,documento_cliente))
		cnx.commit()
		cur.close()
		return 'Editado';

	CORS(app)
	@app.route('/editar_producto', methods=['PUT'])
	def edit_pro():
		cur = cnx.cursor(buffered=True)
		data = request.get_json(force=True)
		id_producto = data.get('id_producto')
		nombre_producto = data.get('nombre_producto')
		descripcion = data.get('descripcion')
		precio = data.get('precio')
		cur.execute('update producto set nombre_producto = %s, descripcion = %s, precio = %s where id_producto = %s', (nombre_producto,descripcion,precio,id_producto))
		cnx.commit()
		cur.close()
		return 'Editado';

	CORS(app)
	@app.route('/editar_pedido', methods=['PUT'])
	def edit_ped():
		cur = cnx.cursor(buffered=True)
		data = request.get_json(force=True)
		numero_orden = data.get('numero_orden')
		fecha = data.get('fecha')
		cliente_documento = data.get('cliente_documento')
		empaquetado = data.get('empaquetado')
		domicilio = data.get('domicilio')
		vendedor = data.get('vendedor')
		cur.execute('update pedido set fecha = %s, cliente_documento = %s, empaquetado = %s, domicilio = %s, vendedor = %s where numero_orden = %s', (fecha,cliente_documento,empaquetado,domicilio, vendedor, numero_orden))
		cnx.commit()
		cur.close()
		return 'Editado';

	CORS(app)
	@app.route('/eliminar_usuarios', methods=['DELETE'])
	def eliminar_user():
		cur = cnx.cursor(buffered=True)
		data = request.get_json(force=True)
		documento = data.get('documento')
		cur.execute('delete from usuario where documento="{}"'.format(documento))
		cnx.commit()
		cur.close()
		print('Eliminado')
		return 'Eliminando';

	CORS(app)
	@app.route('/eliminar_cliente', methods=['DELETE'])
	def eliminar_client():
		cur = cnx.cursor(buffered=True)
		data = request.get_json(force=True)
		documento_cliente = data.get('documento_cliente')
		cur.execute('delete from cliente where documento_cliente="{}"'.format(documento_cliente))
		cnx.commit()
		cur.close()
		print('Eliminado')
		return 'Eliminando';

	CORS(app)
	@app.route('/eliminar_producto', methods=['DELETE'])
	def eliminar_prod():
		cur = cnx.cursor(buffered=True)
		data = request.get_json(force=True)
		id_producto = data.get('id_producto')
		cur.execute('delete from producto where id_producto="{}"'.format(id_producto))
		cnx.commit()
		cur.close()
		print('Eliminado')
		return 'Eliminando';

	CORS(app)
	@app.route('/eliminar_pedido', methods=['DELETE'])
	def eliminar_ped():
		cur = cnx.cursor(buffered=True)
		data = request.get_json(force=True)
		numero_orden = data.get('numero_orden')
		cur.execute('delete from pedido where numero_orden="{}"'.format(numero_orden))
		cnx.commit()
		cur.close()
		print('Eliminado')
		return 'Eliminando';

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)	

app.run(host='0.0.0.0')