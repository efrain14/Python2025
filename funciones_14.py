""" FUNCIONES USANDO UNA FUNCION CON UN BUCLE WHILE Y AÑADIENDO UNA CONDICION PARA SALIR DEL BUCLE INFINITO 
hay un problema con este bucle while: no hemos definido una
condiciön para salir. Dönde pones una condiciön para dejar de
fumar cuando pides una serie de entradas? Queremos que el usuario
pueda salir lo mås fåcilmente posible, por lo que cada mensaje debe
ofrecer una forma de salir. La instrucciön break ofrece una forma
sencilla de salir del bucle en cualquiera de los dos mensajes:"""

def formato_nombre(primer_nombre, apellido):
    """ funcion que formateas el nombre de una persona"""
    nombre_completo = f"{primer_nombre} {apellido}"
    return nombre_completo.title()

while True:
    print("\nPor favor digame su nombre: ")
    print("Introduce 'q' en cualquier momento para salir.")
    
    primer_N = input("Primer Nombre: ")
    if primer_N == 'q':
        break
    apellido1 = input("apellido: ")
    if apellido1 == 'q':
        break
    
    nombre_formateado = formato_nombre(primer_N, apellido1)
    print(f"\nHola, {nombre_formateado}")
