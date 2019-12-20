#programa para hallar la placa de un carro
import libreria
import os
#INPUT
placa=os.sys.argv[1]

# PROC
# 1. La placa tiene 6 caracteres
# 2. La placa debe tener numeros y letras
if ( len(placa) == 6 ):
    if ( placa.isalnum() == True ):
        resultado = placa + " es valido"
    else:
        resultado = placa + " es invalido (no es un alfanumerico)"
    #fin_if
else:
    resultado = placa + " es invalido (no tiene 6 caracteres)"
#fin_if

# OUT
print(resultado)
