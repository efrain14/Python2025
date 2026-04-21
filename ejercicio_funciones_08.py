"""PRUEBELO USTED MISMO  FUNCIONES 8-7 SEGUNDA PARTE
Utilice None para agregar un paråmetro opcional a crear_album() que le permita
almacenar la cantidad de canciones en un ålbum. Si la linea de llamada incluye un
valor para la cantidad de canciones, agregue ese valor al diccionario del ålbum. Realice
al menos una nueva llamada de funcion que incluya la cantidad de canciones de un
ålbum."""


def crear_album(n_artista, n_album, n_canciones= None):
    artista_album = {"Nombre del cantante" : n_artista, "Nombre del album" : n_album }
    if n_canciones:
        artista_album ["numero de canciones"] = n_canciones
    return artista_album
cantante = crear_album("rafael", "16 grandes exitos", "16")
print(cantante)
cantante = crear_album("carlos mata", "primer album")
print(cantante)
cantante = crear_album("roberto carlos" , "canciones de amor", 12)
print(cantante)