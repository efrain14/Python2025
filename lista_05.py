""""3-6. Más invitados: Acabas de encontrar una mesa más grande, así que ahora hay más espacio disponible. Piensa en tres invitados más para invitar a cenar.
• Comienza con el programa del Ejercicio 3-4 o 3-5. Agrega una llamada a print() al final del programa para informar a los usuarios que encontraste una mesa más grande.
• Usa insert() para agregar un nuevo invitado al principio de tu lista.
• Usa insert() para agregar un nuevo invitado al centro de tu lista.
• Usa append() para agregar un nuevo invitado al final de tu lista.
• Imprime un nuevo conjunto de mensajes de invitación, uno para cada persona de tu lista."""

lista_invitados = ["efrain", "luis","junior", "alexis", "jose"]
print(lista_invitados)
lista_invitados.insert(0, "ersy")
lista_invitados.insert(2, "maria")
lista_invitados.append("carlet")
print(lista_invitados)
print("\nseñores invitados se ha encontrado una meza mas grande y por ello invitaremos a mas personas")
print("\n")
print("-*"* 30)
invitacion = "usted ha sido cordialmente invitado para la cena de esta noche"
print("\nseñora",lista_invitados[0],invitacion)
print("\nseñor",lista_invitados[1],invitacion)
print("\nseñora",lista_invitados[2],invitacion)
print("\nseñor",lista_invitados[3],invitacion)
print("\nseñor",lista_invitados[4],invitacion)
print("\nseñor",lista_invitados[5],invitacion)
print("\nseñor",lista_invitados[6],invitacion)
print("\nseñora",lista_invitados[7],invitacion)
cadena1 = "Hola, mundo!\nEsto es una nueva línea."
print(cadena1)

print("-" * 20) # Separador para mejor visualización

# Ejemplo 2: Múltiples saltos de línea
cadena2 = "Primera línea.\nSegunda línea.\nTercera línea."
print(cadena2)

print("-" * 20) # Separador

# Ejemplo 3: Salto de línea al inicio o al final (aunque menos común)
cadena3 = "\nEsta línea comienza con un salto."
print(cadena3)

cadena4 = "Esta línea termina con un salto.\n"
print(cadena4)