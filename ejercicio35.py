"""
Crea la clase UsuarioBanco
Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
Código a seguir:
Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
Implementar agregar_dinero para aumentar el saldo del usuario.
Caso de uso:
        a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
        b. Agregar 20 unidades al saldo de Bob.
        c. Transferir 80 unidades de Bob a Alicia.
        d. Retirar 50 unidades del saldo de Alicia.

"""

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        # Inicializar un usuario con nombre, saldo y un indicador de cuenta corriente
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        # Implementar agregar_dinero para aumentar el saldo del usuario
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que cero.")
        self.saldo += cantidad
        print(f"[{self.nombre}] Se agregaron {cantidad} unidades. Saldo actual: {self.saldo}")

    def retirar_dinero(self, cantidad):
        # Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible
        if cantidad > self.saldo:
            raise ValueError(f"Error en [{self.nombre}]: Fondos insuficientes para retirar {cantidad} unidades. Saldo disponible: {self.saldo}")
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero.")
            
        self.saldo -= cantidad
        print(f"[{self.nombre}] Se retiraron {cantidad} unidades. Saldo actual: {self.saldo}")

    def transferir_dinero(self, usuario_destino, cantidad):
        # Implementar transferir_dinero para transferir dinero hacia otro usuario (restando de este y sumando al destino)
        print(f"\n--- Iniciando transferencia: {self.nombre} -> {usuario_destino.nombre} por {cantidad} unidades ---")
        
        # Primero intentamos retirar el dinero de la cuenta origen
        try:
            self.retirar_dinero(cantidad)
        except ValueError as e:
            # Si falla el retiro por fondos insuficientes, lanzamos un error de transferencia fallida
            raise ValueError(f"Transferencia fallida: {e}")
            
        # Si el retiro fue exitoso, agregamos el dinero al usuario destino
        usuario_destino.agregar_dinero(cantidad)
        print(f"--- Transferencia completada con éxito ---\n")


#Caso de uso

try:
    # a. Crear dos usuarios: "Alicia" con saldo de 100 y "Bob" con saldo de 50, ambos con cuenta corriente.
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    print("a. Usuarios creados con éxito.")
    print(f"   Saldo inicial Alicia: {alicia.saldo} | Saldo inicial Bob: {bob.saldo}\n")

    # b. Agregar 20 unidades al saldo de Bob.
    print("b. Ejecutando agregar_dinero en Bob:")
    bob.agregar_dinero(20)
    print()

    # c. Transferir 80 unidades de Bob a Alicia.
    # Nota: Bob tiene 50 + 20 = 70 unidades. Intentar transferir 80 lanzará un error.
    print("c. Intentando transferir 80 unidades de Bob a Alicia:")
    bob.transferir_dinero(alicia, 80)

    # d. Retirar 50 unidades del saldo de Alicia.
    # (Este paso no se ejecutará en la secuencia normal porque el paso 'c' lanza una excepción que interrumpe el flujo)
    print("d. Intentando retirar 50 unidades de Alicia:")
    alicia.retirar_dinero(50)

except ValueError as error:
    print(f"\n⚠️ Se capturó una excepción en el sistema: {error}")