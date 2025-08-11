"""listas vacias"""
nombres = ["jose", "carlos", "admin", "luis", "pedro"]
for nombre in nombres:
    print(f"bienvenido sr.{nombre}")
print("\n")
for nombre in nombres:
    if nombre == "admin":   
        print(f"Hola {nombre} desea ver un informe del estado?")
    else:
        print(f"Hola {nombre}, gracias por volver a iniciar sesion")
