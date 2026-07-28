#Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

try:

    def buscar_nombre():
    # Solicitamos la lista de nombres separados por comas
        entrada_nombres = input("Ingresa una lista de nombres separados por comas: ")
    
        # Convertimos la entrada en una lista y limpiamos los espacios en blanco de cada nombre
        lista_nombres = [nombre.strip() for nombre in entrada_nombres.split(",")]
    
        #Solicitamos el nombre a buscar
        nombre_a_buscar = input("Ingresa el nombre que deseas buscar: ").strip()
    
        #Comprobamos si el nombre existe en la lista
        if nombre_a_buscar in lista_nombres:
         print(f"¡Éxito! El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
        else:
         #Si no está, lanzamos nuestra propia excepción con un mensaje personalizado
            raise ValueError(f"Error: El nombre '{nombre_a_buscar}' no se encuentra en la lista.")

except ValueError as error:
    print(f"Se capturó una excepción controlada -> {error}")

# Ejecutamos la función
print (buscar_nombre())

