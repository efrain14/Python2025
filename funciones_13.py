""" USANDO UNA FUNCION CON UN BUCLE WHILE 
Puedes usar funciones con todas las estructuras de Python que has
aprendido hasta ahora. Por ejemplo, usemos la funci6n get_formatted_name () con un bucle while para saludar a los usuarios de manera mås formal. Aqui hay un primer intento de saludar a las personas usando su nombre y apellido:"""

def formato_nombre(primer_nombre, apellido):
    """funcion para formatear en nombre de una persona"""
    nombre_completo =f"{primer_nombre} {apellido}"
    return nombre_completo.title()

# esto es un bucle infinito
while True:
    print("\nPor favor dime tu nombre:")
    primer_N = input("Primer nombre ")
    apellido1 = input("apellido ")
    nombre_formateado = formato_nombre(primer_N, apellido1)
    print(f"\nHola, {nombre_formateado}")