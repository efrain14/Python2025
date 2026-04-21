"""PRUEBELO USTED MISMO  8-6 
Nombres de ciudades: escriba una funciön llamada ciudad_pais() que tome el
nombre de una ciudad y su pais. La funcion deberia devolver una cadena con el
formato siguiente:  "Santiago, Chile"
Llame a su funci6n con al menos tres pares de ciudad-pais e imprima los valores que
se devuelven."""
def ciudad_pais(ciudad, pais):
    """funcion que da formato al nombre de una ciudad y el pais deonde se encuentra"""
    ciudad_pais = f"{ciudad} : {pais}"
    return ciudad_pais.title()
ciudadpais = ciudad_pais("valencia", "venezuela")
print(ciudadpais)
ciudadpais = ciudad_pais("bogota", "colombia")
print(ciudadpais)
ciudadpais = ciudad_pais("lima", "peru")
print(ciudadpais)