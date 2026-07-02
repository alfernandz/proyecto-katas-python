#Crea una función lambda que calcule el resto de la división entre dos números dados.

#Creamos las variables para los dos números
numero1 = 30
numero2 = 7

#en la función lambda declaramos dos variables y lo que debe hacer la función con ambas variables
resto = lambda a,b: a%b

#imprimimos la función con los dos números como parámetros

print (resto(numero1,numero2))