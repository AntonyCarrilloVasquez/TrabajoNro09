#programa para calcular la presion
import libreria
import os

fuerza=int(os.sys.argv[1])
area=int(os.sys.argv[2])

s=libreria.presion(fuerza,area)
print("la presion que ejerce un liquido sobre la pelota es:",s)
