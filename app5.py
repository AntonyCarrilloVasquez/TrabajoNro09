#programa para hallar el tiempo de encuentro entre 2 vehiculos
import libreria
import os

v1=int(os.sys.argv[1])
v2=int(os.sys.argv[2])
distancia=int(os.sys.argv[3])

b=libreria.tiempo_encuentro(v1,v2,distancia)
print("el tiempo de encuentro entre 2 vehiculos es:",b)
