"""FUNCIONES  
puede ampliar fácilmente la función contruye_persona() para aceptar valores opcionales como un segundo nombre, una edad, una ocupación o cualquier otra
información que desee almacenar sobre una persona. Por ejemplo, el siguiente cambio también le permite almacenar la edad de una persona:"""

def construye_persona(primer_nombre, apellido, edad=None):
    """ funcion que ordena en un diccionario los nobres y edades de una persona"""
    persona = {"Nombre" : primer_nombre, "Apellido" : apellido, }
    if edad:
        persona["edad"] = edad
        return persona
    
trabajador = construye_persona("pedro", "briceño", edad = 40)
print(trabajador)