'''
Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
    a. Solicitar al usuario el precio original de un artículo.
    b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    e. Mostrar el precio final de la compra, considerando o no el descuento.
    f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
'''

def calcular_monto_final():
    print("--- SISTEMA DE PAGO DE LA TIENDA EN LÍNEA ---")
    
    try:
        # a. Solicitar al usuario el precio original de un artículo.
        precio_original = float(input("Introduce el precio original del artículo (€): "))
        
        if precio_original <= 0:
            print(" Error: El precio del artículo debe ser mayor a cero.")
            return

        # b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        # f. Usar estructuras de control de flujo (if, elif, else)
        if tiene_cupon == "sí" or tiene_cupon == "si":
            # c. Solicitar el valor del cupón de descuento (asumimos que es un porcentaje, ej: 15 para 15%)
            valor_cupon = float(input("Introduce el porcentaje de descuento del cupón (1-100): "))
            
            # d. Aplicar el descuento siempre que el valor del cupón sea válido (mayor a cero y menor o igual a 100)
            if 0 < valor_cupon <= 100:
                descuento = precio_original * (valor_cupon / 100)
                precio_final = precio_original - descuento
                print("\n--- Recibo de Compra (Con Descuento) ---")
                print(f"Precio original: {precio_original:.2f}€")
                print(f"Descuento aplicado ({valor_cupon}%): -{descuento:.2f}€")
            else:
                print("\n El cupón no es válido (debe ser un porcentaje entre 1 y 100).")
                precio_final = precio_original
                print("\n--- Recibo de Compra (Sin Descuento) ---")
                
        elif tiene_cupon == "no":
            precio_final = precio_original
            print("\n--- Recibo de Compra (Sin Descuento) ---")
            
        else:
            print("\n Respuesta no válida. Se asumirá que no tienes un cupón.")
            precio_final = precio_original
            print("\n--- Recibo de Compra ---")

        # e. Mostrar el precio final de la compra
        print(f"Monto final a pagar: {precio_final:.2f}€")
        print("---------------------------------------")

    except ValueError:
        print("Error: Por favor, ingresa un número numérico válido para los precios o cupones.")

# Ejecutamos el programa
calcular_monto_final()