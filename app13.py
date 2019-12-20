#programa para hallar el telefono
import os
#INPUT
TELEFONO=os.sys.argv[1]

# PROC
# 1. El telefono tiene 9 caracteres
# 2. El telefono solo tiene numeros
if ( len(TELEFONO) == 9 ):
    if ( TELEFONO.isdigit() == True ):
        resultado = TELEFONO + " es valido"
    else:
        resultado = TELEFONO + " es invalido (no es un numero)"
    #fin_if
else:
    resultado = TELEFONO + " es invalido (no tiene 9 caracteres)"
#fin_if

# OUT
print(resultado)
