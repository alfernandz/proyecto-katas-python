#Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto_empleado(nombre_completo, lista_empleados):
    # Pasamos el nombre buscado a minúsculas y quitamos espacios extra al inicio/final
    nombre_buscado = nombre_completo.strip().lower()
    
    # Recorremos la lista de empleados uno por uno
    for empleado in lista_empleados:
        # Comparamos el nombre del empleado actual (también en minúsculas)
        if empleado["nombre"].lower() == nombre_buscado:
            return empleado["puesto"]  # Si lo encuentra, devuelve el puesto inmediatamente
            
    # Si el bucle termina y no encontró coincidencias, devuelve el mensaje de error
    return "La persona no trabaja aquí."