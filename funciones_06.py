""" VALORES PREDETERMINADOS 
Al escribir una función, puede definir un valor predeterminado para
cada parámetro. Si se proporciona un argumento para un parámetro
en la llamada a la función, Python usa el valor del argumento. De lo
contrario, utiliza el valor predeterminado del parámetro. Entonces,
cuando defines un valor predeterminado para un parámetro, puedes
excluir el argumento correspondiente que normalmente escribirías
en la llamada a la función. El uso de valores predeterminados puede
simplificar las llamadas a funciones y aclarar las formas en que se
utilizan normalmente las funciones.
Por ejemplo, si observa que la mayoría de las llamadas a descrive_mascota()
se utilizan para describir perros, puede establecer el
valor predeterminado de animal_type en 'perro'. Ahora cualquiera que
llame a describe_mascota() o para pedir un perro puede omitir esa
información:"""
def descrive_mascota(nombre_mascota, tipo_animal = "perro"):
    """muestra informacion de las mascotas"""
    print(f"\nmi mascota es un {tipo_animal}")
    print(f"mi {tipo_animal} se llama {nombre_mascota} .")
    
descrive_mascota(nombre_mascota="puzo")


#Nota
#Cuando utiliza valores predeterminados, cua/quier paråmetro
#con un valor predeterminado debe aparecer después de todos
#los paråmetros que no tienen valores predeterminados. Esto
#permite que Python continue interpretando argumentos
#posicionales correctamente.
