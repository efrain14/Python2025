""" PRUEBELO USTED MISMO  FUNCIONES  8-7 
Álbum: escriba una función llamada crear_album()  que cree un diccionario que
describa un álbum de música. La función debe incluir el nombre de un artista y el título
de un álbum, y debe devolver un diccionario que contenga estos dos datos. Utilice la
función para crear tres diccionarios que representen diferentes álbumes. Imprima cada
valor de retorno para mostrar que los diccionarios almacenan la información del álbum
correctamente."""

def crear_album(n_artista, n_album):
    artista_album = {"Nombre del cantante" : n_artista, "Nombre del album" : n_album }
    return artista_album
cantante = crear_album("rafael", "16 grandes exitos")
print(cantante)
cantante = crear_album("carlos mata", "primer album")
print(cantante)
cantante = crear_album("roberto carlos" , "canciones de amor")
print(cantante)
