"""RECORRIENDO TODOS LOS VALORES DE UN DICCIONARIO"""

lenguajes_favoritos = {
    "jose" : "python",
    "pedro" : "rust",
    "maria" : "java",
    "alexander" : "PHP",
    "violeta" : "python"
    
    }
print("los siguientes lenguajes fueron mencionados en la encuesta:")
for lenguaje in set(lenguajes_favoritos.values()): # al envolver con set la coleccion de valores los elementos duplicados y repetidos se eliminan y solo queda uno
    print(lenguaje.title())