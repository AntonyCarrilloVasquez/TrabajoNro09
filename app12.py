#programa para hallar trapecio
import libreria
import os

base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])

o=libreria.trapecio(base_mayor,base_menor)
print("el trapecio es:",o)
