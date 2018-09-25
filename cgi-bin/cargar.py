#! /usr/bin/python
# -*- coding: utf-8 -*-
import cgi, time
import dbm

fecha = time.strftime("%d-%m-%y")
ultimos_datos = dbm.open("/tmp/%s" % fecha, "c")
guardar = dbm.open("db/base", "c")

form = cgi.FieldStorage() 
dato1 = form.getvalue('dato1')
dato2 = form.getvalue('dato2')
dato3 = form.getvalue('dato3')
dato4 = form.getvalue('dato4')
mensaje = form.getvalue('msj')

hora = time.strftime("%H:%M:%S")

info_device = None

if dato1 is None or dato2 is None:
    temperatura = ultimos_datos.get("temperatura")
    humedad = ultimos_datos.get("humedad")
    luz = ultimos_datos.get("luz")
    suelo = ultimos_datos.get("suelo")
    aviso = ultimos_datos.get("mensaje")

else:
    ultimos_datos["temperatura"] = dato1
    ultimos_datos["humedad"] = dato2
    ultimos_datos["luz"] = dato3
    ultimos_datos["suelo"] = dato4
    ultimos_datos["mensaje"] = mensaje
    temperatura = dato1
    humedad = dato2
    luz = dato3
    suelo = dato4
    aviso = mensaje
    guardar["(%s)-%s"% (fecha, hora)] = str([temperatura, humedad, luz, suelo])

ultimos_datos.close()
guardar.close()

print "Content-type:text/html; charset=utf-8\r\n\r\n"
#print "%s" % info_device
        


    
    
