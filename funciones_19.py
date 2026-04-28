""" FUNCIONES  
Uso de argumentos de palabras clave arbitrarios
A veces querrás aceptar una cantidad arbitraria de argumentos, pero no sabrás de
antemano qué tipo de información se pasará a la función. En este caso, puede 
escribir funciones que acepten tantos pares clave-valor como proporcione la 
declaración de llamada. Un ejemplo implica la creación de perfiles de usuario: 
sabes que obtendrás información sobre un usuario, pero no estás seguro de qué tipo
de información recibirás. La función hecer_perfil() en el siguiente ejemplo siempre toma un nombre
y apellido, pero también acepta una cantidad arbitraria de argumentos de palabras
clave:"""
#perfil_usuario.py

def hacer_perfil(nombre, apellido, **info_usuario):
    """contruye un diccionario que contiene toda la informacion de un usuario"""
    info_usuario["primer_nombre"]= nombre
    info_usuario["Primer_apellido"]= apellido
    return info_usuario

perfil_usuario = hacer_perfil("alber", "einstein", lugar="princeton", materia="fisica")
print(perfil_usuario)
