"""
Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
"""
def determinar_momento_dia():
    try:
        # Solicitamos la hora al usuario y la convertimos a entero
        hora = int(input("Introduce la hora actual (0 a 23): "))
        
        # Validamos que la hora sea correcta
        if hora < 0 or hora > 23:
            print("❌ Error: La hora debe estar entre 0 y 23.")
            return

        # Lógica para determinar el momento del día
        # De 6:00 a 12:59 -> Día (Mañana)
        if 6 <= hora < 13:
            print("🌅 ¡Es de día! (Mañana)")
            
        # De 13:00 a 20:59 -> Tarde
        elif 13 <= hora < 21:
            print("🌆 ¡Es de tarde!")
            
        # De 21:00 a 5:59 -> Noche
        else:
            print("🌃 ¡Es de noche!")
            
    except ValueError:
        print("❌ Error: Por favor, introduce un número entero válido.")

# Ejecutamos la función
determinar_momento_dia()
