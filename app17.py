#programa para hallar el numero de casa
import libreria
import os
#INPUT
casa=os.sys.argv[1]

# PROC
# 1. la casa tiene 3 caracteres
# 2. El dni solo tiene numeros
if ( len(casa) == 3 ):
    if ( casa.isdigit() == True ):
        resultado = casa + " es valido"
    else:
        resultado = casa + " es invalido (no es un numero)"
    #fin_if
else:
    resultado = casa + " es invalido (no tiene 3 caracteres)"
#fin_if

# OUT
print(resultado)
