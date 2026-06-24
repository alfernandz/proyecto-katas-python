#Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.
def realizar_division():
    try: #este es el bloque que se ejecutará y puede producir algún error

        # Pedimos los datos al usuario y los convertimos a decimales (float)
        numerador = float(input("Introduce el primer número (dividendo): "))
        denominador = float(input("Introduce el segundo número (divisor): "))
        
        # Realizamos la división
        resultado = numerador / denominador
        
    except ValueError:
        # Este bloque se ejecutará si el usuario introduce letras o símbolos que no son números
        print("\n Error: Debes introducir un valor numérico válido.")
        print("Estado: Operación fallida.")
        
    except ZeroDivisionError:
        # este bloque se ejecutará si el denominador es 0
        print("\n Error: No es posible dividir entre cero.")
        print("Estado: Operación fallida.")
        
    else:
        # Este bloque se ejecutará ÚNICAMENTE si no ocurrió ninguna excepción en el bloque try
        print(f"\n✅ ¡División exitosa!")
        print(f"El resultado de {numerador} entre {denominador} es: {resultado}")

# Ejecutamos el programa
realizar_division()