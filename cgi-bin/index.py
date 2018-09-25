#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time, cgi
import cargar, os
import dbm

src = cgi.FieldStorage() 
link = src.getvalue("")

fecha = time.strftime("%d-%m-%y")

menu_items = (["MONITOR", ""],
              ["REGISTRO", "ver"],
              ["PARAMETROS", "param"])

def get_valores():
    base = dbm.open("db/base", "r")
    j = len(base.keys()) - 1
    print "<div id=centrado>"
    print "<h2>Ultimos 10 registros</h2>"
    for i in range(10):
        n = j - i
        print "<h3>%s</h3>" % base.keys()[n]
        print '<p>Temperatura: %s °C<p>' % eval(base.get(base.keys()[n]))[0]
        print '<p>Humedad ambiente: %s °/.<p>' % eval(base.get(base.keys()[n]))[1]
        print '<p>Luz: %s °/.<p>' % eval(base.get(base.keys()[n]))[2]
        print '<p>Humedad suelo: %s °/.<p>' % eval(base.get(base.keys()[n]))[3]
    print "</div>"
    base.close()

def menu():
    print '<div class="menu">'
    for i in range(len(menu_items)):
        print '<a href="?=%s">' % menu_items[i][1]
        print '<button>%s</button></a>' % menu_items[i][0]
    print '</div>'

print "<html>"
print "<head>"
print '<link media="all" href="/data/pagina.css" type="text/css" rel="stylesheet">'
print '<meta name="viewport" content="width=device-width, initial-scale=1.0">'

if link == "ver":
    print "<title>Registros</title>"
    print "</head>"
    print '<body><div id="contenedor"><div class="cabecera">'
    print '<img src="/data/banner.png"/>'
    print '<h2>REGISTRO DE DATOS</h2></div>'
    print '<div class="menu_principal">'
    menu()
    print '<div class="contenido">'
    get_valores()
    print '</div></div><BR><BR>'
    print '<div class="pie">%s</div></body>' % fecha
    print "</html>"
    
elif link == "param":
    print "<title>Modifica Parametros</title>"
    print "</head>"
    print '<body><div id="contenedor"><div class="cabecera">'
    print '<img src="/data/banner.png"/>'
    print '<h2>MODIFICA LOS PARAMETROS</h2></div>'
    print '<div class="menu_principal">'
    menu()
    print '<div class="contenido">'
    print '<div id="centrado"><BR>'
    print '<form action = "get.py" method = "get">'
    print '<p>Seleciona el parametro:</p>'
    print '<select name = "parametro">'
    print '<option value = "temperatura" selected>Temp Maxima</option>'
    print '<option value = "humedad" selected>Humedad Minima</option>'
    print '<option value = "luz" selected>Luz Minima</option>'
    print '<option value = "suelo" selected>Humedad suelo Min</option>'
    print '</select><br><br>'
    print '<p>Ingresa un valor 0-100:</p>'
    print '<input type="number" name="valor" min="0" max="100" step="1"><br><br>'
    print '<br><button>APLICAR</button></form>'
    print '</div></div></div></div><BR><BR>'
    print '<div class="pie">%s</div></body>' % fecha
    print "</html>"
    
else:
    print """ <meta http-equiv="refresh" content="3"/>"""
    print "<title>Monitor Invernadero</title>"
    print "</head>"
    print '<body><div id="contenedor"><div class="cabecera">'
    print '<img src="/data/banner.png"/>'
    print '<h2>RECIBIENDO DATOS</h2></div>'
    print '<div class="menu_principal">'
    menu()
    print '<div class="contenido"><div id="centrado">'
    print '<BR>'
    print '<BR><H3>TEMPERATURA :  <a style="color:green;">%s °C</a></H3>' % (cargar.temperatura)
    print '<BR><H3>HUMEDAD AIRE:  <a style="color:green;">%s °/.</a></H3>' % (cargar.humedad)
    print '<BR><H3>LUMINICIDAD:  <a style="color:green;">%s °/.</a></H3>' % (cargar.luz)
    print '<BR><H3>HUMEDAD SUELO:  <a style="color:green;">%s °/.</a></H3>' % (cargar.suelo)
    print '<BR><BR><BR>'
    print '</div></div><div class="lateral"><h3>AVISO!</h3><p>Dispositivo encendido:'
    print '</p><h2><a style="color:green;">%s</a></h2></div>' % (cargar.aviso)
    print '</div></div></div><BR>'
    print '<div class="pie"><BR>%s</div></body>' % (cargar.hora)
    print "</html>"


