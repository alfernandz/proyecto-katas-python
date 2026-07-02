#Crea una función que cuente el número de caracteres en una cadena de texto dada.

#usamos una función lambda para contar los caracteres
numero_caracteres= lambda cadena: len (cadena)

#creamos la cadena de texto que usaremos para contar los caracteres
cadena_texto = "Los programadores evolucionarán pero no desaparecerán"

#imprimimos la función incluyendo como parámetro la cadena de texto (cadena_texto)
print (numero_caracteres (cadena_texto))