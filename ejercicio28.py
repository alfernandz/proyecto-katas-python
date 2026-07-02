#Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def elemento_duplicado (lista):
    elementos_recorridos = set() # creamos una variable que será un set en el que se guardarán los elementos recorridos

    for elemento in lista: #creamos un bucle for para recorrer la lista
        if elemento in elementos_recorridos: #condición para realizar una acción si el elemento se encuentra en el set
            return elemento #si se cumple la condición, la función devuelve el elemento que se repite
        elementos_recorridos.add (elemento) #si no se cumple, se añade al conjunto

    return None #si el bucle no encuentra elementos duplicados, devuelve None



lista_duplicado = [5,10,15,5,14,9]

print (elemento_duplicado(lista_duplicado))