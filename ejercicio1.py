""""
Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
"""
def contar_frecuencia_letras_manual(cadena): #creamos la función con una cadena de texto como parámetro
    frecuencias = {}
    for letra in cadena.lower(): #creamos el bucle para recorrer cada carácter de la cadena
        if letra != " ":  # ignoramos los espacios
            frecuencias[letra] = frecuencias.get(letra, 0) + 1 # Si la letra ya existe, suma 1; si no, la inicializa en 0 y suma 1
    return frecuencias
