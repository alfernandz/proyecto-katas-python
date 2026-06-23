# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def evaluar_rendimiento(lista_notas, nota_aprobado=5):
    # Validación por si la lista está vacía
    if not lista_notas:
        return (0.0, "suspenso")
    
    # Calculamos la media de las notas
    media = sum(lista_notas) / len(lista_notas)
    
    # Determinamos el estado según la media
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
        
    # Devolvemos la tupla con la media (redondeada a 2 decimales) y el estado
    return (round(media, 2), estado)