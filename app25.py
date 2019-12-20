#programa para hallar el costo fijo medio
import libreria
import os

costo_fijo=int(os.sys.argv[1])
produccion=int(os.sys.argv[2])

M=libreria.costo_fijo_medio(costo_fijo,produccion)
print("el costo fijo medio es:",M)

