#!/usr/bin/env python
import cgi, time
import dbm

fecha = time.strftime("%d-%m-%y")
base_de_datos = dbm.open("db/parametro", "c")

ultimo_parametro = []

form = cgi.FieldStorage()
parametro = form.getvalue('parametro')
valor = form.getvalue('valor')

try:
    lista = base_de_datos.keys()
    for i in range(len(lista)):
        ultimo_parametro.append(base_de_datos.get(lista[i]))
except:
    ultimos_parametros = [None, None]
    pass
                      

if valor is None or parametro is None:
    print "Content-type:text/html; charset=utf-8\r\n\r\n"
    print '%s' % ultimo_parametro
else:
    base_de_datos['parametro'] = parametro
    base_de_datos['valor'] = valor
    ultimos_parametro = [parametro, valor]
    print "Content-type:text/html; charset=utf-8\r\n\r\n"
    print '<meta http-equiv="Refresh" content="1;url=/cgi-bin/index.py?=param" />'

