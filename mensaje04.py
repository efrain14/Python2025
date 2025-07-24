"""
eliminacion de espacios en blanco adicionales en los lados derecho e isquierdo
de una cadena utilizando el metodo rstrip():para el lado derecho y el metodo
istrip() para el lado isquierdo y para ambos lados a la vez se usa el metodo strip() """

lenguaje_favorito = "python "
print(lenguaje_favorito)
lenguaje_favorito.rstrip()
print(lenguaje_favorito.rstrip())
print(lenguaje_favorito)
lenguaje_favorito = lenguaje_favorito.rstrip()
print(lenguaje_favorito)

lenguaje_favorito = " python "
print(lenguaje_favorito)
lenguaje_favorito = lenguaje_favorito.strip()
print(lenguaje_favorito)
