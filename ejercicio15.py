#Crea una función lambda que sume 3 a cada número de una lista dada.

#Creamos la lista de números
numeros_suma = [4, 8, 16, 32, 64]

#Creamos una variable que incluirá la función lambda
suma_tres = list(map(lambda x: x+3, numeros_suma))

print (suma_tres)