#Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# 1. Definimos una excepción personalizada para el rango de edad
class EdadFueraDeRangoError(Exception):
    """Excepción lanzada cuando la edad no está entre 0 y 120 años."""
    def __init__(self, edad, mensaje="Error: La edad debe estar entre 0 y 120 años."):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# 2. Función principal del programa
def pedir_edad():
    try:
        # Pedimos el dato al usuario y lo transformamos a entero
        entrada = input("Por favor, introduce tu edad: ")
        edad = int(entrada)
        
        # Validamos si la edad está en el rango correcto
        if edad < 0 or edad > 120:
            raise EdadFueraDeRangoError(edad)
            
    except ValueError:
        # Se ejecuta si el usuario introduce letras, decimales o símbolos
        print("❌ Error: Debes introducir un número entero válido.")
        
    except EdadFueraDeRangoError as e:
        # Se ejecuta si el número está fuera de 0 - 120
        print(f"❌ {e.mensaje} (Introdujiste: {e.edad})")
        
    else:
        # Se ejecuta solo si todo el bloque 'try' funcionó a la perfección
        print(f"✅ Edad registrada con éxito. Tienes {edad} años.")

# Ejecutamos el programa
pedir_edad()