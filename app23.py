#programa para calcular la fuerza elastica
import libreria
import os

deformacion=int(os.sys.argv[1])
constante=int(os.sys.argv[2])

l=libreria.fuerza_elastica(deformacion,constante)
print("la fuerza elastica es:",l)
