""" PASAR UNA LISTA 
A menudo le resultarå ütil pasar una lista a una funciön, ya sea una
lista de nombres, nümeros u objetos mås complejos, como
diccionarios. Cuando pasa una lista a una funcion, la funcion obtiene
acceso directo al contenido de la lista. Usemos funciones para hacer
que trabajar con listas sea mås eficiente.
Digamos que tenemos una lista de usuarios y queremos imprimir un
saludo para cada uno. El siguiente ejemplo envia una lista de
nombres a una funcin llamada saludos_usuarios()  que saluda a cada
persona de la lista individualmente:"""

def saludos_usuarios(nombres):
    """funcion para usar una lista y enviar un saludo a los integrantes de la lista"""
    for nombre in nombres:
        mensaje = f"Hola, {nombre.title()}"
        print(mensaje)
        
nombreusuarios = ["jose", "junior", "maria"]
saludos_usuarios(nombreusuarios)