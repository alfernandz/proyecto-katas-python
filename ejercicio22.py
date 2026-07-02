#Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

#importamos la función reduce
from functools import reduce

#Creamos la lista con los números que se multiplicarán
lista_22 = [5,10,16,23,31]

#creamos la función lambda con el reduce incorporado
#acumulación guarda las multiplicaciones acumuladas
#elemento es cada uno de los números de la lista (efectivamente, cada elemento)
producto = reduce (lambda acumulación, elemento: acumulación*elemento, lista_22)

#imprimimos la variable para comprobar que la función es correcta
print (producto)
