#Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

def enmascarar_texto(variable):
    # Convertimos la variable a string
    texto = str(variable)
    
    # Si el texto tiene 4 caracteres o menos, no hace falta enmascarar nada
    if len(texto) <= 4:
        return texto
    
    # Cambiamos por (#) todos los caracteres menos los últimos cuatro
    # Luego concatenamos los últimos 4 caracteres sin cambiar nada
    return "#" * (len(texto) - 4) + texto[-4:]

#ejemplo para aplicar la función
tarjeta = 1234567812345678
print(enmascarar_texto(tarjeta))