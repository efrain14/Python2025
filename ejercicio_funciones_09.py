""" PRUEBELO USTED MISMO  FUNCIONES  8-8 
Álbumes de usuario: comience con su programa del Ejercicio 8-7. Escribe un bucle
while que permita a los usuarios ingresar el artista y el título de un álbum. Una vez
que tenga esa información, llame a crear_album()  con la entrada del usuario e imprima
el diccionario creado. Asegúrese de incluir un valor de salida en el bucle while."""

def crear_album(n_artista, n_album):
    """funcion que ordena los nonbres de artista y del album"""
    artista_album = f"{n_artista} : {n_album}"
    return artista_album.title()
while True:
    print("\npor favor escribe el nombre del artista:")
    print("oprime 'q' si quieres abandonar la insercion")
    
    n_artista = input("Nombre del artista ")
    if n_artista == "q" :
        break
    
    n_album = input("Nombre del album ")
    if n_album == "q" :
        break
    
    artista_album =crear_album(n_artista, n_album)
    print(f"\nInformacion del Album {artista_album}")