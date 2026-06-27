#Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

from functools import reduce

def digitos_a_numero(lista_digitos):
    # Si la lista está vacía, devolvemos 0 para evitar errores
    if not lista_digitos:
        return 0
    
    # reduce() va acumulando el resultado aplicando la fórmula matemática
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, lista_digitos)

#Ejemplo para comprobar la función
digitos = [5, 7, 2]
resultado = digitos_a_numero(digitos)

print(resultado)
print(type(resultado)) 