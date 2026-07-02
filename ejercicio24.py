#Calcula la diferencia total en los valores de una lista. Usa la función reduce().

#importamos la función reduce
from functools import reduce

#creamos la lista
lista_diferencia = [50,20,10,5]

#para la función lambda, declaramos dos variables, que serán la cantidad que se va restando (a) y el elemento que se restará (b)
diferencia = reduce(lambda a,b: a-b, lista_diferencia)

#imprimimos para comprobar que funciona correctamente
print (diferencia)