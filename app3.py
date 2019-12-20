#programa para hallar el peso de una persona
import libreria
import os

masa=int(os.sys.argv[1])
gravedad=int(os.sys.argv[2])

c=libreria.peso(masa,gravedad)
print("el peso de una persona es:",c)
