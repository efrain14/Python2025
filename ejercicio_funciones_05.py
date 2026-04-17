"""PRUEBELO USTED MISMO  FUNCIONES 8-5 
Ciudades: Escriba una funcion llamada describe_ciudad() que ecepte el nombre de
una ciudad y su pais. la funcion deberia imprimir una oracion simple como Bogota
esta en colombia. Asigne el parametro del pais un valor predeterminado. Llame
a su funcion para 3 ciudades diferentes, al menos una de las cuales no este en
el pais predeterminado"""

def describe_ciudad(ciudad, pais = "Venezuela") :
    """funcion que mustra una ciudad y el pais donde esta"""
    print(f"\nla ciudad de: {ciudad} esta ubicada en {pais}")
describe_ciudad("valencia")
describe_ciudad("Caracas")
describe_ciudad("Lima", pais= "Peru")