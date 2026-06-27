#Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

# 1. Creamos la lista de diccionarios con la información de los estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificación": 85},
    {"nombre": "Carlos", "edad": 22, "calificación": 92},
    {"nombre": "María", "edad": 21, "calificación": 90},
    {"nombre": "Juan", "edad": 23, "calificación": 78},
    {"nombre": "Elena", "edad": 20, "calificación": 95}
]

# 2. Usamos filter() para extraer los que tienen calificación >= 90
# Convertimos el resultado final en una lista con list()
estudiantes_excelentes = list(
    filter(lambda estudiante: estudiante["calificación"] >= 90, estudiantes)
)

# 3. Mostramos el resultado de forma limpia
print("--- Estudiantes con calificación mayor o igual a 90 ---")
for est in estudiantes_excelentes:
    print(f"Nombre: {est['nombre']} | Edad: {est['edad']} | Calificación: {est['calificación']}")