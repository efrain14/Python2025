""" Ejemplo 2: Recetas e Ingredientes (Múltiples Claves con Listas)
Aquí usamos listas para registrar los ingredientes de varias recetas. """

# Crear un diccionario donde cada clave es una receta y el valor es su lista de ingredientes
recetario = {
    'Pesto Casero': ['Albahaca', 'Piñones', 'Aceite de Oliva', 'Parmesano', 'Ajo'],
    'Sopa de Lentejas': ['Lentejas', 'Zanahoria', 'Apio', 'Caldo de Verduras'],
    'Brownies de Chocolate': ['Harina', 'Cacao en Polvo', 'Mantequilla', 'Azúcar', 'Huevo']
}

print("--- Recetas Disponibles ---")

# 1. Iterar sobre las claves (nombres de recetas)
for receta, ingredientes in recetario.items():
    print(f"\nReceta: **{receta}**")
    
    # 2. Iterar sobre la lista de ingredientes para cada receta
    print("Ingredientes:")
    for ingrediente in ingredientes:
        print(f"  - {ingrediente}")