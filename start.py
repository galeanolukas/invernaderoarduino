#!/usr/bin/env python
import subprocess, os
import arduino_conect
os.system("./pycgi-server start")
p = subprocess.Popen(["chromium", "http://localhost:8000"])
conexion = arduino_conect.GetData()
p.wait()
os.system("./pycgi-server stop")
conexion.exit()

