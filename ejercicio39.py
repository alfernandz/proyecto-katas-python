'''
Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).
'''

import math

def calcular_area(figura, datos):
    # Convertimos el texto a minúsculas para evitar problemas de formato
    figura = figura.lower()
    
    if figura == "rectangulo":
        # Desempaquetamos la tupla en base y altura
        base, altura = datos
        return base * altura
        
    elif figura == "triangulo":
        # Desempaquetamos la tupla en base y altura
        base, altura = datos
        return (base * altura) / 2
        
    elif figura == "circulo":
        # El círculo solo requiere el radio
        radio = datos[0]
        return math.pi * (radio ** 2)
        
    else:
        return "Figura no válida. Elige entre 'rectangulo', 'circulo' o 'triangulo'."


# --- PRUEBA DEL CÓDIGO ---

# Rectángulo: base = 8, altura = 4
print("Área rectángulo:", calcular_area("rectangulo", (8, 4)))

# Triángulo: base = 10, altura = 5
print("Área triángulo:", calcular_area("triangulo", (10, 5)))

# Círculo: radio = 5
print("Área círculo:", round(calcular_area("circulo", (5,)), 2))