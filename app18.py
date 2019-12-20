#programa para hallar la aceleracion
import libreria
import os

velocidad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

f=libreria.aceleracion(velocidad,tiempo)
print("la aceleracion de un corredor es:",f)

