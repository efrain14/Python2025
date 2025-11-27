"""pruebelo usted mismo 5-9 listas vacias"""
nombres = []
if nombres:
    for nombre in nombres:
        if nombre == "admin":   
            print(f"Hola {nombre} desea ver un informe del estado?")
        else:
            print(f"Hola {nombre}, gracias por volver a iniciar sesion")
else:
    print("nesesitamos conseguir algunos usuarios")

