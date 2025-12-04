""" dicionarios con bucles for """

trabajador01 = {
        "nombre" : "pedro",
        "apellido" : "briceno",
        "edad" : 48,
        "ciudad": "valencia",
}

for key, valor in trabajador01.items():
    print(f"\nkey: {key}")
    print(f"valor: {valor}")

print("\n LENGUAJES DE PROGRAMACION")    
lenguajes_favoritos = {
    "jose" : "pithon",
    "pedro" : "rust",
    "maria" : "java",
    "alexander" : "PHP",
    }
for nombre, lenguaje in lenguajes_favoritos.items():
    print(f"\nnombre: {nombre.title()}")
    print(f"lenguage: {lenguaje.title()}")
print("\n")

for nombre, lenguaje in lenguajes_favoritos.items():
    print(f"soy {nombre.title()} y mi lenguaje de programacion favorito es: {lenguaje.title()}")