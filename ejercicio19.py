#Crea una función lambda que filtre los números impares de una lista dada.

#Primero, creamos la lista de números con pares e impares mezclados
numeros_impares = [4,6,7,8,11,16,19,22,25]

#La función lambda contiene varios aspectos importantes:
# - list para devolver el resultado en una lista
# - filter para filtrar los números impares
# - x: x%2 !=0 es la condición que eliminará los números pares (aquellos que divididos entre dos devuelven un resto de 0)
# - numeros_impares es la lista a la que se aplicará la función
filtro_impares = list(filter(lambda x: x%2!=0, numeros_impares))

#comprobamos que la función funciona correctamente
print (filtro_impares)