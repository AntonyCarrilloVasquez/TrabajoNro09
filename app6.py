#programa para ver el sueldo de una persona
import libreria
import os

tiempo=int(os.sys.argv[1])
horas_trabajadas=int(os.sys.argv[2])
impuestos=int(os.sys.argv[3])

v=libreria.sueldo(tiempo,horas_trabajadas,impuestos)
print("el sueldo de Juan es:",v)

