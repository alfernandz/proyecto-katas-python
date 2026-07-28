'''
Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
Reglas:
        0 - 69: insuficiente
        70 - 79: bien
        80 - 89: muy bien
        90 - 100: excelente
'''
def evaluar_calificacion():
    try:
        # Solicitamos la nota al usuario (puede incluir decimales usando float)
        nota = float(input("Introduce la calificación numérica del alumno (0 a 100): "))
        
        # Validamos que la nota esté dentro del rango permitido
        if nota < 0 or nota > 100:
            print("Error: La calificación debe estar entre 0 y 100.")
            return

        # Aplicamos las reglas de evaluación
        if 0 <= nota <= 69:
            resultado = "insuficiente"
        elif 70 <= nota <= 79:
            resultado = "bien"
        elif 80 <= nota <= 89:
            resultado = "muy bien"
        else:
            # Si no entra en los anteriores, por descarte está entre 90 y 100
            resultado = "excelente"
            
        print(f"La calificación del alumno es: {resultado.upper()}")

    except ValueError:
        print("❌ Error: Por favor, introduce un número válido.")

# Ejecutamos el programa
evaluar_calificacion()