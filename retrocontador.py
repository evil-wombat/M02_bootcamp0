# Recursividad: Función que se llama a sí misma.

def retrocontador (e):
    print ("{}, ".format(e), end= "")
    
# Importante dar una condición de salida, si no entra en un bucle infinito
    if e > 0:
        retrocontador (e-1)

retrocontador (10)


def sumatorio (n):
    if n != 0:
        return n + sumatorio (n-1)
    else:
        return 0

sumatorio (4)