#Concatena una lista de palabras. Usa la función reduce().

from functools import reduce
lista_palabras = ['la','casa','está','domotizada']

concatenacion = reduce(lambda a,b: a+" "+b, lista_palabras)

print (concatenacion)