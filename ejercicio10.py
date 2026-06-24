#Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# 1. Definimos la excepción personalizada
class ListaVaciaError(Exception):
    def __init__(self, mensaje="Error: No se puede calcular el promedio de una lista vacía."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


# 2. Creamos la función que calcula el promedio
def calcular_promedio(numeros):
    # Si la lista está vacía (evalúa como False), lanzamos nuestra excepción
    if not numeros:
        raise ListaVaciaError()
    
    # Si tiene elementos, calcula y devuelve el promedio
    return sum(numeros) / len(numeros)

# ejemplo para comprobar la función
# Caso 1: Lista con números (Éxito)
notas = [8, 9, 10, 7]

try:
    resultado = calcular_promedio(notas)
    print(f"✅ El promedio es: {resultado}")
except ListaVaciaError as e:
    print(f"❌ Ocurrió un error controlado: {e}")

print("-" * 30)

# Caso 2: Lista vacía (Salta la excepción)
datos_vacios = []

try:
    resultado = calcular_promedio(datos_vacios)
    print(f"✅ El promedio es: {resultado}")
except ListaVaciaError as e:
    print(f"❌ Ocurrió un error controlado: {e}")
