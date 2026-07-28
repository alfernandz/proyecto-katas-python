# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabras_que_contienen(lista_palabras, palabra_objetivo):
    # Usamos una lista de comprensión para filtrar las palabras
    # .lower() asegura que la búsqueda no sea sensible a mayúsculas/minúsculas
    return [
        palabra for palabra in lista_palabras 
        if palabra_objetivo.lower() in palabra.lower()
    ]

#Ejemplo de uso
lista_frutas =['manzana', 'pera', 'fresa', 'kiwi', 'naranja', 'pera', 'limón']
palabra_objetivo = 'pera'
print (buscar_palabras_que_contienen(lista_frutas, palabra_objetivo))