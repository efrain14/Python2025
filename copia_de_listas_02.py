"""4-10. Porciones: Usando uno de los programas que escribiste en este capítulo, agrega varias líneas al final del programa que hagan lo siguiente:
• Imprimir el mensaje "Los primeros tres elementos de la lista son:". Luego, usa una porción para imprimir los tres primeros elementos de la lista de ese programa.
• Imprimir el mensaje "Los tres primeros elementos del centro de la lista son:". Luego, usa una porción para imprimir tres elementos del centro de la lista.
• Imprimir el mensaje "Los últimos tres elementos de la lista son:". Luego, usa una porción para imprimir los tres últimos elementos de la lista.

4-11. Mis pizzas, tus pizzas: Comienza con tu programa del Ejercicio 4-1 (página 56).
Haz una copia de la lista de pizzas y llámala friend_pizzas. Luego, haz lo siguiente:
• Agregar una nueva pizza a la lista original.
• Agregar una pizza diferente a la lista friend_pizzas.
• Demuestra que tienes dos listas separadas. Imprime el mensaje "Mis pizzas favoritas son:" y luego usa un bucle for para imprimir la primera lista. Imprime el mensaje "Las pizzas favoritas de mi amigo son:" y luego usa un bucle for para imprimir la segunda lista.
Asegúrate de que cada nueva pizza se guarde en la lista correspondiente.
4-12. Más bucles: Todas las versiones de foods.py en esta sección han evitado el uso de bucles for al imprimir para ahorrar espacio. Elige una versión de foods.py y escribe dos bucles for para imprimir cada lista de alimentos."""

mis_comidas = ["pizza", "arepas", "cachapas", "pasta", "arroz", "caraotas"]
print("Los primeros alimentos que mas me gustan son:")
print(mis_comidas[:3])
print("\nLos tres elementos del medio de la lista son:")
print(mis_comidas[2:5])
print("\nLos tres ultimos elementos de la lista son:")
print(mis_comidas[-3:])
pizzas = ["margarita", "calzone", "pepperoni", "vegetariana"]
pizzas_amigos = pizzas[:]
pizzas.append("especial")
pizzas_amigos.append("4estaciones")
print("\nMis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza.title())
print("\nlas pizzas favoritas de mis amigos son:")    
for pizza in pizzas_amigos:
    print(pizza.title())
