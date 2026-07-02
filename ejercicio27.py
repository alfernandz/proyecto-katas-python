#Crea una función que calcule el promedio de una lista de números.

def media_numeros (lista):
    contador = 0
    suma_total = 0
    for elemento in lista:
        suma_total += elemento
        contador += 1
    
    return suma_total / contador
    

lista_numeros = [5,15,20,25,35]
print (media_numeros(lista_numeros))