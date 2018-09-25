#!/usr/bin/env python
import os, serial
import threading, urllib2
import time

class GetData(threading.Thread):
    def __init__(self, url="http://localhost:8000/cgi-bin/cargar.py?"):
        threading.Thread.__init__(self)
        self.server = url + "dato1=%s&dato2=%s&dato3=%s&dato4=%s&msj=%s"
        self.puerto = None
        self.puertos = ["ttyUSB", "ttyACM"]
        self.disp = None
        self.data = None
        self.ultimo_parametro = [None, None]
        self.detener_bucle = False
        self.start()
        
    def run(self):
        while 1:
            time.sleep(2)
            if self.device_plug():
                print "Dispositivo Conectado al %s" % self.puerto
                self.send_data()
                self.send_param()
            else:
                print "Dispositivo Desconectado"
                pass
            
    def device_plug(self):
        dev = os.listdir("/dev/")
        for i in range(5):
            if self.puertos[0] + str(i) in dev:
                self.puerto = self.puertos[0] + str(i)
                return True
                break
        
            elif self.puertos[1] + str(i) in dev:
                self.puerto = self.puertos[1] + str(i)
                return True
                break
            
            else:
                return False
                pass

    def send_data(self):
        try:
            self.disp = serial.Serial("/dev/" + self.puerto)
            self.data = eval(self.disp.readline())
            print self.data
            urllib2.urlopen(self.server % (self.data[0], self.data[1], self.data[2], self.data[3], self.data[4]))
            self.disp.close()
        except:
            pass
        
    def send_param(self):
        nuevo = urllib2.urlopen("http://localhost:8000/cgi-bin/get.py").read()
        if eval(nuevo) == self.ultimo_parametro:
            print "No se escribio parametro"
            pass
        else:
            print "nuevo parametro %s" % nuevo
            self.ultimo_parametro = eval(nuevo)
            self.disp = serial.Serial("/dev/" + self.puerto)
            self.disp.write("%s=%s" % (eval(nuevo)[1], eval(nuevo)[0]))
            self.disp.close()
            
    def exit(self):
        self.detener_bucle = True
        


            
            
        
        

            
    
    
