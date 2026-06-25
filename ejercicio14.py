#Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
def filtrar_por_letra_inicial(lista_palabras, letra_objetivo):
    # Aseguramos que la letra objetivo esté en minúscula para la comparación
    letra_objetivo = letra_objetivo.lower()
    
    # filter() evalúa cada palabra: palabra[0].lower() obtiene la primera letra
    # list() convierte el resultado final en una lista
    return list(filter(lambda palabra: palabra and palabra[0].lower() == letra_objetivo, lista_palabras))


#Ejemplo para comprobar la función
palabras = ["Manzana", "perro", "Mesa", "gato", "melón", "Libro"]
letra = "m"

resultado = filtrar_por_letra_inicial(palabras, letra)
print(resultado)