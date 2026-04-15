"""ARGUMENTOS DE PALABRA CLAVE 
Un argumento de palabra clave es un par nombre-valor que se pasa
a una función. Usted asocia directamente el nombre y el valor dentro
del argumento, de modo que cuando pasa el argumento a la
función, no hay confusión. Los argumentos de palabras clave le liberan de tener 
que preocuparse por ordenar correctamente sus argumentos en la
llamada a la función y aclaran la función de cada valor en la llamada
a la función. Reescribamos mascotas.py usando argumentos de palabras clave
para llamar a descrive_mascota():  """

def descrive_mascota(tipo_animal, nombre_mascota) :
    """muestra informacion sobre mascotas"""
    print(f"\n yo tengo un {tipo_animal}.")
    print(f"\n mi {tipo_animal} se llama {nombre_mascota.title()}.")
descrive_mascota(tipo_animal="perro", nombre_mascota="puzo")
descrive_mascota(nombre_mascota="harry", tipo_animal="gato", )