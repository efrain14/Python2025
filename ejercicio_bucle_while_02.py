"""              7-5. Entradas de cine: 
una sala de cine cobra diferentes precios de entradas segün la
edad de la persona. Si es menor de 3 años, la entrada es gratuita; 
si tienen entre 3 y 12 años, el boleto cuesta $10; y si son mayores de 12 años
la entrada cuesta $15. Escribe un bucle en el que preguntes a los usuarios su 
edad y luego les digas el coste de su entrada al cine."""

prompt = "\nque edad tienes "

prompt += "\nEscribe salir cuando ayas terminado  "

# BUCLE INFINITO PARA PREGUNTAR EDADES CONTINUAMENTE
while True:
# CONDICION PARA CERRAR EL PROGRAMA    
    edad = input(prompt)
    if edad.lower() == "salir" :
        break
    
# CONVERTIMOS LA EDAD EN UN NUMERO ENTERO
    edad = int(edad)
    
# LOGICA DE LOS PRECIOS POR EDADES
    if edad < 3:
        print(" La entrada es gratuita para menores de 3 años,")
    elif edad <=  13 :
        print("El precio de tu entrada es de $ 10")
    else:
        print(" El precio de tu entrada es de $15")   
        
    print("-"*30)     # SEPARADOR VISUAL
    print("Disfruta de la Pelicula")