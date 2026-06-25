#Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

def longitud_de_palabras(frase):
    # 1. Usamos frase.split() para convertir "Hola Mundo" en ["Hola", "Mundo"]
    # 2. Con map(len, ...) aplicamos la función len() a cada palabra de esa lista
    # 3. list(...) convierte el resultado en una lista
    return list(map(len, frase.split()))