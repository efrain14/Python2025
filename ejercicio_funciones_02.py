""" PRUEBELO USTED MISMO  8-2 
Libro favorito: escriba una función llamada libro_favorito() que acepte un
parámetro, title(). La función debería imprimir un mensaje, como uno de mis libros 
favoritos es el nombre de la rosa. Llame a la función, asegurándose de incluir el 
título de un libro como argumento en la llamada a la función."""

def  libro_favorito(nombre_libro) :
    """muestra mis libros favorito"""
    print(f"el libro :{nombre_libro.title()}, es uno de mis libros favoritos")
libro_favorito("las mil y una noches")