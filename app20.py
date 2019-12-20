#programa para hallar el area de un circulo
import libreria
import os

pi=int(os.sys.argv[1])
radio=int(os.sys.argv[2])

h=libreria.area_circulo(pi,radio)
print("el area de un circulo es:",h)
