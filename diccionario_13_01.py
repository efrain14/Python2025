"""MODIFICAR LA LISTA DE ALIENIGENAS CREADA EN DICCIONARIO_12.PY
DANDOLES DIFERENTES CARACTERISTICAS MEDIANTE EL BUCLE FOR Y AGREGANDO  ELIF"""

aliens = []
for numero_alien in range(30):
    nuevos_aliens = {"color" : "amarillo", "puntos" : 5, "velocidad" : "lenta"}
    aliens.append(nuevos_aliens)

for alien in aliens[0:3]:
    if alien ["color"] == "verde":
        alien["color"] = "amarillo"
        alien["velocidad"] = "media"
        alien["puntos"] = 10
    elif alien["color"] == "amarillo" :
        alien["color"] = "rojo"
        alien["velocidad"] = "rapida"
        alien["puntos"] = 15
for alien in aliens[:5]:   # mustra los 5 primeros aliens
    print(alien)
        