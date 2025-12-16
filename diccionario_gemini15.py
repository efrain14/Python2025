""" Ejemplo 3: Manejo de Datos de un Juego (Modificación y Existencia)
Este ejemplo muestra cómo verificar si un elemento existe en la lista y cómo modificar un elemento específico."""

# Diccionario para un jugador de un videojuego
datos_jugador = {
    'usuario': 'MasterCoder2025',
    'nivel': 55,
    'inventario': ['Espada de Fuego', 'Armadura de Acero', 'Poción de Vida', 'Mapa Antiguo']
}

# 1. Verificar si tiene un objeto en su inventario
if 'Poción de Vida' in datos_jugador['inventario']:
    print("\n¡El jugador tiene Poción de Vida en su inventario!")
else:
    print("\nLe falta la Poción de Vida.")

# 2. Reemplazar un objeto (usando el índice)
# La 'Armadura de Acero' está en el índice 1 de la lista 'inventario'
indice_armadura = 1 
datos_jugador['inventario'][indice_armadura] = 'Armadura de Diamante'
print(f"Inventario después de la mejora: {datos_jugador['inventario']}")