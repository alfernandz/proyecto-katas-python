#Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().
def mapear_letras_unicas(caracteres):
    # 1. Usamos set() para eliminar cualquier letra repetida y filtrar espacios
    caracteres_unicos = set(c for c in caracteres if c != " ")
    
    # 2. map() toma cada letra y devuelve la tupla (Mayúscula, Minúscula)
    return list(map(lambda letra: (letra.upper(), letra.lower()), caracteres_unicos))