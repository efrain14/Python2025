"""LISTAS DE DICCIONARIO
primero creamos 3 diccionarios, cada uno de los cuales representa un extraterrestre diferente. almacenamos cada uno de estos diccionarios en una lista llamada aliens, recorremos la lista e imprimimos cada alien"""

alien01 = {"color" : "verde", "puntos" : 5}
alien02 = {"color" : "amarillo", "untos" : 10}
alien03 = {"color" : "rojo", "puntos" : 15}

aliens = [alien01, alien02, alien03]
for alien in aliens:
    print(alien)