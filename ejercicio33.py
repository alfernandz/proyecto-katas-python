#Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# Definimos la función utilizando map y lambda
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# Ejemplo de uso:
lista_a = [1, 2, 3, 4]
lista_b = [5, 6, 7, 8]

resultado = sumar_listas(lista_a, lista_b)
print(resultado)