""""
Crea una función llamada procesar_texto
Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
Código a seguir:
Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
Caso de uso:
Verificar el funcionamiento completo de procesar_texto.
"""

def contar_palabras(texto):
    #Cuenta el número de veces que aparece cada palabra en el texto.
    palabras = texto.lower().split()
    diccionario_conteo = {}
    
    for palabra in palabras:
        # Limpiamos signos de puntuación básicos adheridos a las palabras
        palabra_limpia = palabra.strip(",.¡!¿?()")
        if palabra_limpia:
            diccionario_conteo[palabra_limpia] = diccionario_conteo.get(palabra_limpia, 0) + 1
            
    return diccionario_conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Sustituye una palabra_original por una palabra_nueva en el texto."""
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra_a_eliminar):
    """Elimina una palabra específica del texto."""
    palabras = texto.split()
    # Filtramos la lista para mantener solo las palabras que no coincidan con la que queremos borrar
    palabras_filtradas = [p for p in palabras if p.strip(",.¡!¿?()") != palabra_a_eliminar]
    return " ".join(palabras_filtradas)


# --- Función Principal ---

def procesar_texto(texto, opcion, *args):
    """
    Recibe un texto, una opción y un número variable de argumentos (*args)
    según la opción elegida.
    """
    if opcion == "contar":
        return contar_palabras(texto)
        
    elif opcion == "reemplazar":
        # Verificamos que se hayan pasado los 2 argumentos necesarios (original y nueva)
        if len(args) < 2:
            raise ValueError("La opción 'reemplazar' requiere dos argumentos adicionales: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
        
    elif opcion == "eliminar":
        # Verificamos que se haya pasado el argumento de la palabra a eliminar
        if len(args) < 1:
            raise ValueError("La opción 'eliminar' requiere un argumento adicional: la palabra a eliminar.")
        return eliminar_palabra(texto, args[0])
        
    else:
        return "Opción no válida. Elige entre 'contar', 'reemplazar' o 'eliminar'."


#Caso de uso

texto_prueba = "Python es un lenguaje genial. Python es fácil de aprender."

print("--- TEXTO ORIGINAL ---")
print(texto_prueba)
print("-" * 30)

# 1. Probar la opción de "contar"
resultado_contar = procesar_texto(texto_prueba, "contar")
print("\n1. Resultado de 'contar':")
print(resultado_contar)

# 2. Probar la opción de "reemplazar"
# Pasamos 'Python' y 'JavaScript' como *args adicionales
resultado_reemplazar = procesar_texto(texto_prueba, "reemplazar", "Python", "JavaScript")
print("\n2. Resultado de 'reemplazar' (Python por JavaScript):")
print(resultado_reemplazar)

# 3. Probar la opción de "eliminar"
# Pasamos 'fácil' como el *args adicional
resultado_eliminar = procesar_texto(texto_prueba, "eliminar", "fácil")
print("\n3. Resultado de 'eliminar' (la palabra 'fácil'):")
print(resultado_eliminar)