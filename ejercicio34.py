
class Arbol:
    def __init__(self):
        # Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # Aumentar la longitud del tronco en una unidad.
        self.tronco += 1

    def nueva_rama(self):
        # Agregar una nueva rama de longitud 1 a la lista de ramas.
        self.ramas.append(1)

    def crecer_ramas(self):
        # Aumentar en una unidad la longitud de todas las ramas existentes.
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        # Eliminar una rama en una posición específica.
        # Validamos que la posición exista en la lista (usando índices de Python: 0, 1, 2...)
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print(f"Error: No existe ninguna rama en la posición {posicion}.")

    def info_arbol(self):
        # Devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }


# Diferentes usos

# a. Crear un árbol.
mi_arbol = Arbol()
print("a. Árbol creado.")

# b. Hacer crecer el tronco una unidad.
mi_arbol.crecer_tronco()
print("b. El tronco ha crecido.")

# c. Añadir una nueva rama.
mi_arbol.nueva_rama()
print("c. Se ha añadido una nueva rama.")

# d. Hacer crecer todas las ramas una unidad.
mi_arbol.crecer_ramas()
print("d. Las ramas existentes han crecido.")

# e. Añadir dos nuevas ramas.
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
print("e. Se han añadido dos nuevas ramas.")

# f. Retirar la rama situada en la posición 2.

mi_arbol.quitar_rama(2)
print("f. Se ha retirado la rama en la posición 2.")

# g. Obtener información sobre el árbol.
informacion = mi_arbol.info_arbol()
print("\ng. Información final del árbol:")
print(f"   - Longitud del tronco: {informacion['longitud_tronco']}")
print(f"   - Número de ramas: {informacion['numero_ramas']}")
print(f"   - Longitud de cada rama: {informacion['longitudes_ramas']}")