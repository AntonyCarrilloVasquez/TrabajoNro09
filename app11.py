#programa para pedir DNI
import libreria
import os
#INPUT
dni=os.sys.argv[1]

# PROC
# 1. El Dni tiene 8 caracteres
# 2. El dni solo tiene numeros
if ( len(dni) == 8 ):
    if ( dni.isdigit() == True ):
        resultado = dni + " es valido"
    else:
        resultado = dni + " es invalido (no es un numero)"
    #fin_if
else:
    resultado = dni + " es invalido (no tiene 8 caracteres)"
#fin_if

# OUT
print(resultado)

