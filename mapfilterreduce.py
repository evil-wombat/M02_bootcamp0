from functools import reduce  

lista = [1, 3, -1, 15, 9]

def doble (x):
    return 2*x

#el operador map actua sobre cada elemento de la lista en orden de posición
listaDobles = map ((lambda x: x*2), lista)
#igual que listaDobles pero con funciones de 1º nivel.
listaDobles1 = map (doble, lista)          


def esPar (x):
    if x%2 == 0:
        return x
    else:
        return None

#filtra en la lista la condición elegida. En este caso si dvidimos entre dos que el resto sea 0.
listaPares = filter (lambda x: x%2 == 0, lista)
#igual que listaPares pero con funciones de 1º nivel
listaPares1 = filter (esPar, lista)             


#reduce la lista a un valor. Por ejemplo sumar todos los valores de una lista.
sumatorio = reduce (lambda x, y: x+y, lista)

suma100 = reduce (lambda x,y: x+y, range (101))

#imprimimos resultados
print (list (listaDobles))
print (list (listaDobles1))

print (list (listaPares))
print (list (listaPares1))

print (sumatorio)
print (suma100)