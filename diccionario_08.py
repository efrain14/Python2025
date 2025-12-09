""" recorriendo todas las claves de un diccionario  02"""

lenguajes_favoritos = {
    "jose" : "pithon",
    "pedro" : "rust",
    "maria" : "java",
    "alexander" : "PHP",
    }

amigos = ["pedro", "alexander"]
for nombre in lenguajes_favoritos.keys():
    print(f"hola {nombre.title()}")

    if nombre in amigos:
        lenguaje = lenguajes_favoritos[nombre]
        print(f"\t{nombre}(, yo uso mucho a {lenguaje} como mi principal lenguaje de programacion)")