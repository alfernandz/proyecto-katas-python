#Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial_recursivo(n):
    # si n es 0 o 1, devolvemos 1
    if n == 0 or n == 1:
        return 1
    
    #Si el dato de entrada no es 0 o 1, la función se llama a sí misma con (n - 1)
    else:
        return n * factorial_recursivo(n - 1)
    

print (factorial_recursivo (5))