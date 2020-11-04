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
    cnx.commit()
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('<head>')
    print('    <meta charset="UTF-8">')
    print('    <title>Concurvas</title>')
    print('    <link rel="stylesheet" href="css/icon/css/fontello.css">')
    print('    <link rel="stylesheet" href="css/menu.css">')
    print('    <link rel="stylesheet" href="css/registro.css">')
    print('    <link rel="stylesheet" href="css/tabla.css">')
    print('    <link href="https://concurvas.com/wp-content/themes/mainteam_Concurvas/imagenes/iconos/concurvas.ico" rel="shortcut icon" type="image/x-icon">')
    print('</head>')
    print('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>')
    print('<body>')
    print('    <main>')
    print('        <div class="content-all">')
    print('            <header></header>')
    print('            <input type="checkbox" id="check">')
    print('            <label id="che" for="check" class="icon-menu">Menu</label>')
    print('            <div id = "logo">')
    print('                <img src="https://concurvas.com/wp-content/themes/mainteam_Concurvas/imagenes/iconos/LOGO.png" alt="Logo Concurvas" id="logol">')
    print('            </div>')
    print('            <nav class="menu">')
    print('                <ul>')
    print('                    <li id="inicio">Inicio</li>')
    print('                    <li id="ventas">Ventas</li>')
    print('                    <li id="empa">Empaquetado</li>')
    print('                    <li id="domici">Domiciliarios</li>')
    print('                    <li id="admin">Admin</li>')
    print('                </ul>')
    print('            </nav>')
    print('        </div>')
    print('    </main>')
    print('<!-- inicio -->')
    print('<div id="ini" style="display: none">')
    print('    <div id="tabla" style="">')
    print('     <div  id = " main-container " >')
    print('            <form action="/cgi-bin/ProyectoArquitecturaBack/tabla.py" method="POST" >    ')
    print('                <table>')
    print('                    <thead>')
    print('                        <tr>')
    print('                            <th>Numero Orden</th>')
    print('                            <th>Fecha</th> ')
    print('                            <th>Cliente</th>')
    print('                            <th>Empaquetado</th> ')
    print('                            <th>Domiciliario</th> ')
    print('                            <th>Vendedor</th>')
    print('                        </tr>')
    print('                    </thead>')
    print('                    <tr>')
    for i in pedido:
        print('<td>{}</td>'.format(i[0]))
        print('<td>{}</td>'.format(i[1]))
        print('<td>{}</td>'.format(i[2]))
        print('<td>{}</td>'.format(i[3]))
        print('<td>{}</td>'.format(i[4]))
        print('<td>{}</td>'.format(i[5]))
    print('                    </tr>')
    print('                </table>')
    print('                <button type="button " class="submit-btn">Registrar</button>')
    print('            </form>')
    print('     </div>')
    print('    </div>')
    print('</div>')
    print('<!-- ventas -->')
    print('<div id="vent" style="display: none">')
    print('    <div class="slidershow middle">')
    print('            <div class="slides">')
    print('                        <input class="avatar" type="radio" name="r" id="r4">')
    print('                     <input class="avatar" type="radio" name="r" id="r5">')
    print('                        <div class="slide s1">')
    print('                            <form action="/cgi-bin/ProyectoArquitecturaBack/registerCliente.py" method="POST" class="form-register">')
    print('                                <h4>Registro Cliente</h4>')
    print('                                <input class="controls" type="text" name="documentoc" placeholder="Documento">')
    print('                                <input class="controls" type="text" name="nombresc" placeholder="Nombre">')
    print('                                <input class="controls" type="text"  name="apellidosc" placeholder="Apellido">')
    print('                                <input class="controls" type="text" name="telefonoc" placeholder="Telefono">')
    print('                                <input class="controls" type="email" name="correoc" placeholder="Correo">')
    print('                                <button type="button " class="submit-btn">Registrar</button>')
    print('                            </form>')
    print('                        </div>')
    print('                        <div class="slide">')
    print('                            <!--formulario de registro de un pedido, en el cual se envian datos y son dirigidos a registerPedido.py-->')
    print('                            <form action="/cgi-bin/ProyectoArquitecturaBack/registerPedido.py" method="POST" class="form-register">')
    print('                                <h4>Registro Pedido</h4>')
    print('                                <input class="controls" type="texto" readonly name="idpe" placeholder="Id Pedido">')
    print('                                <input class="controls" type="text" name="fecha" placeholder="Fecha">')
    print('                                <input class="controls" type="text"  name="documentocl" placeholder="Documento Cliente">')
    print('                                <input class="controls" type="text" name="documentoven" placeholder="Documento Vendedor">')
    print('                                <button type="button " class="submit-btn">Registrar</button>')
    print('                            </form>')
    print('                        </div>')
    print('                    </div>')
    print('                    <div class="navigation">')
    print('                 <label for="r4" class="bar"></label>')
    print('                 <label for="r5" class="bar"></label>')
    print('             </div>')
    print('            </div>')
    print('    </div>')
    print('')
    print('</div>')
    print('')
    print('<!-- empaquetado -->')
    print('<div id="emp" style="display: none">')
    print('    <!--formulario de actualizacion de un pedido, en el cual se envian datos y son dirigidos a empaquetado.py-->')
    print('    <form action="/cgi-bin/ProyectoArquitecturaBack/empaquetado.py" method="POST" class="form-register" style="margin-top: 220px;">')
    print('        <h4>Empaquetado</h4>')
    print('        <input class="controls" type="text" name="documentoem" placeholder="Documento">')
    print('        <input class="controls" type="text" name="numero_pedido" placeholder="Numero del pedido">')
    print('        <button type="button " class="submit-btn">Registrar</button>')
    print('    </form>')
    print('')
    print('</div>')
    print('')
    print('<!-- domiciliario -->')
    print('<div id="domi" style="display: none">')
    print('    <!--formulario de actualizacion de un pedido, en el cual se envian datos y son dirigidos a domiciliario.py -->')
    print('    <form action="/cgi-bin/ProyectoArquitecturaBack/domiciliario.py" method="POST" class="form-register" style="margin-top: 220px;">')
    print('        <h4>Domiciliario</h4>')
    print('        <input class="controls" type="text" name="documentodo" placeholder="Documento">')
    print('        <input class="controls" type="text" name="numero_pedido" placeholder="Numero del pedido">')
    print('        <button type="button " class="submit-btn">Registrar</button>')
    print('    </form>')
    print('')
    print('</div>')
    print('')
    print('</div>')
    print('')
    print('<!-- administracion -->')
    print('    <div id="admi" style="display: none">')
    print('     <div class="slidershow middle">')
    print('         <div class="slides">')
    print('             <input class="avatar" type="radio" name="r" id="r1">')
    print('                 <input class="avatar" type="radio" name="r" id="r2">')
    print('                 <input class="avatar" type="radio" name="r" id="r3">')
    print('                 <div class="slide s1">')
    print('                        <!--formulario del registro de usuario, en el cual se envian datos y son dirigidos a registerUsuario.py -->')
    print('                     <form action="/cgi-bin/ProyectoArquitecturaBack/registerUsuario.py" method="POST" class="form-register">')
    print('                            <h4>Registro Usuario</h4>')
    print('                            <input class="controls" type="text" name="documento" placeholder="Documento">')
    print('                            <input class="controls" type="text" name="nombres" placeholder="Nombre">')
    print('                            <input class="controls" type="text"  name="apellidos" placeholder="Apellido">')
    print('                            <input class="controls" type="text" name="telefono" placeholder="Telefono">')
    print('                            <input class="controls" type="email" name="correo" placeholder="Correo">')
    print('                            <select style = "color:#b55986 !important" class="controls" name="rol" >')
    print('                                <option id="rol" value="0">Rol</option> ')
    print('                                <option value="1">Vendedor</option> ')
    print('                                <option value="2">Domiciliario</option> ')
    print('                                <option value="3">Empacador</option> ')
    print('                            </select>')
    print('                            <input class="controls" type="password" name="contraseña" placeholder="Contraseña">')
    print('                            <button type="button " class="submit-btn">Registrar</button>')
    print('                        </form>')
    print('                 </div>')
    print('                 <div class="slide">')
    print('                        <!--formulario del registro de clientes, en el cual se envian datos y son dirigidos a registerCliente.py -->')
    print('                     <form action="/cgi-bin/ProyectoArquitecturaBack/registerCliente.py" method="POST" class="form-register">')
    print('                            <h4>Registro Cliente</h4>')
    print('                            <input class="controls" type="text" name="documentoc" placeholder="Documento">')
    print('                            <input class="controls" type="text" name="nombresc" placeholder="Nombre">')
    print('                            <input class="controls" type="text"  name="apellidosc" placeholder="Apellido">')
    print('                            <input class="controls" type="text" name="telefonoc" placeholder="Telefono">')
    print('                            <input class="controls" type="email" name="correoc" placeholder="Correo">')
    print('                            <button type="button " class="submit-btn">Registrar</button>')
    print('                        </form>')
    print('                 </div>')
    print('                 <div class="slide">')
    print('                        <!--formulario del registro de productos, en el cual se envian datos y son dirigidos a registerProducto.py -->')
    print('                     <form action="/cgi-bin/ProyectoArquitecturaBack/registerProducto.py" method="POST" class="form-register">')
    print('                            <h4>Registro Producto</h4>')
    print('                            <input class="controls" type="texto" readonly name="idp" placeholder="Id producto">')
    print('                            <input class="controls" type="text" name="nombrep" placeholder="Nombre">')
    print('                            <input class="controls" type="text"  name="descripcionp" placeholder="Descripcion">')
    print('                            <input class="controls" type="text" name="preciop" placeholder="Precio">')
    print('                            <button type="button " class="submit-btn">Registrar</button>')
    print('                        </form>')
    print('                 </div>')
    print('             </div>')
    print('             <div class="navigation">')
    print('                 <label for="r1" class="bar"></label>')
    print('                 <label for="r2" class="bar"></label>')
    print('                 <label for="r3" class="bar"></label>')
    print('             </div>')
    print('         </div>')
    print('        </div>')
    print('    </div>')
    print('</body>')
    print('<script src="js/js.js"> </script>')
    print('</html>')
    
cnx.close()
