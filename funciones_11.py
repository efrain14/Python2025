"""DEVOLVER UN DICCIONARIO 
una funcion puede devolver cualquier tipo de valor que necesite, incluidas 
estructuras de datos mas complicadas como listas y diccionarios, por ejemplo la 
siguiente funcion toma partes de un nombre y devuelve un diccionario que representa
una persona"""
def construlle_persona(primer_nombre, segundo_nombre) :
    """retorna un diccionario con la informacion de una persona"""
    persona = {"primero" : primer_nombre, "segundo" : segundo_nombre}
    return persona

trabajador = construlle_persona("pedro", "briceño")
print(trabajador)
    