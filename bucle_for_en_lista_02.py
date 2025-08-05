"""PRUÉBALO TÚ MISMO
4-1. Pizzas: Piensa en al menos tres tipos de tu pizza favorita. Guarda los nombres de las pizzas 
una lista y luego usa un bucle for para imprimir el nombre de cada pizza.
• Modifica tu bucle for para imprimir una oración con el nombre de la pizza, en lugar de imprimir 
solo el nombre. Para cada pizza, debes tener una línea de salida con una oración simple 
como "Me gusta la pizza de pepperoni".
• Agrega una línea al final de tu programa, fuera del bucle for, que indique cuánto te gusta la 
pizza.La salida debe constar de tres o más líneas sobre los tipos de pizza que te gustan y una 
oración adicional, como "¡Me encanta la pizza!"."""

pizzas = ["margarita", "calzone", "pepperoni", "vegetariana"]

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("Me encanta la pizza de "f"{pizza.title()}")
print("la pizza que mas me gusta es la de", pizzas[2].title())
print("La pizza que menos me gusta es la", pizzas[3].title())
print("me encanta la pizza".title())
# End-of-file (EOF)
