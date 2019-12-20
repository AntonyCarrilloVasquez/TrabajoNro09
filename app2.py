#programa para hallar la densidad
import libreria
import os

masa=int(os.sys.argv[1])
volumen=int(os.sys.argv[2])

y=libreria.densidad(masa,volumen)
print("la densidad de un cuerpo es:",y)
