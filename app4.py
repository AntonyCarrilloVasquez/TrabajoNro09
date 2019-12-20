#programa para calcular la fuerza de una persona
import libreria
import os

masa=int(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])

a=libreria.fuerza(masa,aceleracion)
print("la fuerza de una persona es:",a)
