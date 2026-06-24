#Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

def tuplas_a_strings(lista_tuplas):
    # map() toma cada tupla, convierte sus elementos a string, los une con un espacio
    # y finalmente list() transforma el resultado en una lista.
    return list(map(lambda tupla: ":".join(map(str, tupla)), lista_tuplas))
    #list transforma el resultado en una lista
    #map(str, tupla) convierte los elementeos de cada tupla a string
    #":".join junta los elementos usando un símbolo de dos puntos para separarlos

#ejemplo para comprobar que la función funciona
especialidades = [("Full Stack", 2500), ("Ciberseguridad", 2250), ("Data Analyst", 2100)]

resultado = tuplas_a_strings(especialidades)
print(resultado)
