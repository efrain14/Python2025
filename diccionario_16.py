"""             Un diccionario en un diccionario
Puedes anidar un diccionario dentro de otro diccionario, pero tu
código puede complicarse rápidamente cuando lo haces. Por
ejemplo, si tiene varios usuarios para un sitio web, cada uno con un
nombre de usuario único, puede utilizar los nombres de usuario
como claves en un diccionario. Luego puede almacenar información
sobre cada usuario utilizando un diccionario como valor asociado con
su nombre de usuario. En el siguiente listado, almacenamos tres
datos sobre cada usuario: su nombre, apellido y ubicación.
Accederemos a esta información recorriendo los nombres de usuario
y el diccionario de información asociado con cada nombre de
usuario:     """

usuario = {
    "aeinstein" : {
        "nombre" : "albert",
        "apellido" : "einstein",
        "lugar" : "pricenton",},
    
    "curie" : {
        "nombre" : "marie",
        "apellido" : "curie",
        "lugar" : "paris",},
}

for usuarionombre, usua_info in usuario.items() :
    print(f"\nusuarionombre : {usuarionombre}")
    nombre_completo = f"{usua_info ['nombre']} {usua_info['apellido']}"
    lugar = usua_info['lugar']
    
    print(f"\tnombre completo:  {nombre_completo.title()}")
    print(f"\tlugar : {lugar.title()}")