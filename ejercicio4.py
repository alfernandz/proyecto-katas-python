# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

lista_A = [10, 20, 30, 40]
lista_B = [3, 5, 12, 20]

# map() toma 'x' de lista_A y 'y' de lista_B en cada iteración
diferencias = list(map(lambda x, y: x - y, lista_A, lista_B))

print(diferencias)