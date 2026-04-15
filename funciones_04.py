"""LLAMADAS A FUNCIONES MULTIPLES 
Puede llamar a una función tantas veces como sea necesario.
Describir una segunda mascota diferente requiere solo una llamada más a
describe_mascota( ) :"""

def descrive_mascota(tipo_animal, nombre_mascota) :
    """muestra informacion sobre mascotas"""
    print(f"\n yo tengo un {tipo_animal}.")
    print(f"\n mi {tipo_animal} se llama {nombre_mascota.title()}.")
descrive_mascota("perro", "puzo")
descrive_mascota("gato", "harry")