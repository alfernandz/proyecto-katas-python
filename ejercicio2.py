# Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

# Lista original de números
numeros = [1, 2, 3, 4, 5]

# Usamos map() con una función lambda que multiplica cada x por 2
#Utilizamos list para devolver la función map como lista
duplicados = list(map(lambda x: x * 2, numeros))

#Comprobamos que funciona
print(duplicados)