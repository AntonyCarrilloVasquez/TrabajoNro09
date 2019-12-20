#programa para hallar la velocidad final
import libreria
import os

velocidad_inicial=int(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

d=libreria.velocidad_final(velocidad_inicial,aceleracion,tiempo)
print("la velocidad final de un bus es:",d)
