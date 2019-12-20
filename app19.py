#programa para hallar la capacitancia electrica
import libreria
import os

carga_electrica=int(os.sys.argv[1])
diferencia_potencia=int(os.sys.argv[2])

g=libreria.capacitancia(carga_electrica,diferencia_potencia)
print("la capacitancia electrica tiene como valor:",g)
