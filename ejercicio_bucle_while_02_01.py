""""   7-5. vercion 2 otra forma de hacer el programa  Entradas de cine: 
una sala de cine cobra diferentes precios de entradas segün la
edad de la persona. Si es menor de 3 años, la entrada es gratuita; si tienen entre 3 y 12 años, el boleto cuesta $10; y si son mayores de 12 años la entrada cuesta $15. Escribe un bucle en el que preguntes a los usuarios su edad y luego les digas el coste de su entrada al cine."""

# Bucle infinito para preguntar edades continuamente
while True:
    entrada = input("Por favor, introduce tu edad (o escribe 'salir' para terminar): ")

    # Condición para cerrar el programa
    if entrada.lower() == 'salir':
        print("¡Disfruta la película!")
        break

    # Convertimos la entrada a un número entero
    edad = int(entrada)

    # Lógica de precios
    if edad < 3:
        print("La entrada es gratuita para menores de 3 años.")
    elif edad <= 12:
        print("El precio de tu entrada es $10.")
    else:
        print("El precio de tu entrada es $15.")
    
    print("-" * 30) # Separador visual