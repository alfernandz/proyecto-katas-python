#Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def filtrar_palabras_largas(cadena, n):
    # 1. Separamos el texto en palabras individuales
    palabras = cadena.split()
    
    # 2. filter() evalúa cada palabra y deja pasar solo las que miden más que n
    return list(filter(lambda palabra: len(palabra) > n, palabras))

#Ejemplo para comprobar la función
texto = "Valencia es una ciudad frente al mar Mediterráneo"
limite = 5

resultado = filtrar_palabras_largas(texto, limite)
print(resultado)