""" Puede anidar una lista dentro de un diccionario en cualquier
momento que desee asociar mås de un valor con una ünica clave en
un diccionario. En el ejemplo anterior de los lenguajes de
programaciön favoritos, si almacenåramos las respuestas de cada
persona en una lista, la gente podria elegir mås de un lenguaje
favorito. Cuando recorremos el diccionario, el valor asociado con
cada persona seria una lista de idiomas en lugar de un solo idioma.    """


lenguajes_favoritos = {
    "jose" : ["pithon","rust"],
    "pedro" : [ "rust", "java"],
    "maria" : ["java", "C"],
    "alexander" : ["PHP","python"],
}
for nombre, lenguajes in lenguajes_favoritos.items():
    print(f"\n{nombre.title()} estos son sus lenguajes favoritos:")
    for lenguaje in lenguajes:
        print(f"\t{lenguaje.title()}")