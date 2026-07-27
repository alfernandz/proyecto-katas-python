#Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

# Definimos la función lambda que recibe dos palabras
es_anagrama = lambda palabra1, palabra2: sorted(palabra1.lower()) == sorted(palabra2.lower())

# Ejemplos de uso:
print(es_anagrama("Cara", "Arca"))       # True
print(es_anagrama("Mora", "Roma"))       # True
print(es_anagrama("Hola", "Adios"))      # False