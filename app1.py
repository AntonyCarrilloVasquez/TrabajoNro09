#programa para hallar la distancia
import libreria
import os

velocidad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

x=libreria.distancia(velocidad,tiempo)
print("la distancia entre dos vehiculos es:",x)
