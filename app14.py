#programa para calcular el costo medio
import libreria
import os

costo_total=int(os.sys.argv[1])
produccion=int(os.sys.argv[2])

p=libreria.costo_medio(costo_total,produccion)
print("el costo medio es:",p)
