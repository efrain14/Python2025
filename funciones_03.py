"""" FUNCIONES  ARGUMENTOS POSICIONALES 
Cuando llama a una función, Python debe hacer coincidir cada
argumento en la llamada a la función con un parámetro en la
definición de la función. La forma más sencilla de hacerlo se basa en
el orden de los argumentos proporcionados. Los valores emparejados de esta manera 
se denominan argumentos posicionales. Para ver cómo funciona esto, considere una 
función que muestra información sobre mascotas. La función nos dice qué tipo de 
animal es cada mascota y el nombre de la mascota, como se muestra aquí:"""

def descrive_mascota(tipo_animal, nombre_mascota) :
    """muestra informacion sobre mascotas"""
    print(f"\n yo tengo un {tipo_animal}.")
    print(f"\n mi {tipo_animal} se llama {nombre_mascota.title()}.")
descrive_mascota("perro", "puzo")