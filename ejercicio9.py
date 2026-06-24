#Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

def filtrar_mascotas_legales(lista_mascotas):
    # Lista de especies prohibidas
    prohibidas = ["mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"]
    
    # Filtramos la lista: dejamos pasar el animal si su nombre en minúsculas no está (not in) en 'prohibidas'
    # Lo transformamos en lista con list()
    return list(filter(lambda mascota: mascota.lower() not in prohibidas, lista_mascotas))

#Ejemplo para comprobar la función
mis_mascotas = ["Perro", "Mapache", "Gato", "Cocodrilo", "Loro", "Oso"]

mascotas_validas = filtrar_mascotas_legales(mis_mascotas)
print(mascotas_validas)