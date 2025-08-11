"""ejercicio"""
#Hola administrador: Crea una lista de cinco o más nombres de usuario, incluyendo "admin". Imagina que estás escribiendo código que imprimirá un saludo para cada usuario después de iniciar sesión en un sitio web. Recorre la lista e imprime un saludo para cada usuario.
#• Si el nombre de usuario es "admin", imprime un saludo especial, como "Hola administrador, ¿desea ver un informe de estado?".
#• De lo contrario, imprime un saludo genérico, como "Hola Jaden, gracias por volver a iniciar sesión".
nombres = ["jose", "carlos", "admin", "luis", "pedro"]
for nombre in nombres:
    print(f"bienvenido sr.{nombre}")
print("\n")
for nombre in nombres:
    if nombre == "admin":   
        print(f"Hola {nombre} desea ver un informe del estado?")
    else:
        print(f"Hola {nombre}, gracias por volver a iniciar sesion")