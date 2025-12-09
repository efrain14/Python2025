""" RECORRIENDO LAS CLAVES DE UN DICCIONARIO EN ORDEN PARTICULAR"""

lenguajes_favoritos = {
    "jose" : "pithon",
    "pedro" : "rust",
    "maria" : "java",
    "alexander" : "PHP",
    }
for nombre in sorted(lenguajes_favoritos.keys()):
    print(f"{nombre.title()}, gracias por participar en la encuesta")