#Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

#creamos la lista de strings e int
lista_mixta = [10, "hola", 5, "mundo", 42, "Python", 1]

# filter() evalúa cada elemento y solo deja pasar los que sean de tipo int
lista_enteros = list(filter(lambda x: isinstance(x, int), lista_mixta))

#comprobamos que funciona
print(lista_enteros)