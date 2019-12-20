#programa para hallar la velocidad angular
import libreria
import os

angulo=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

k=libreria.velocidad_angular(angulo,tiempo)
print("la velocidad angular es:",k)
