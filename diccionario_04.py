"""   rastreo de extraterrestre """
# Para un ejemplo más interesante, rastreemos la posición de un extraterrestre que puede moverse a diferentes velocidades. Almacenaremos un valor que represente su velocidad actual y lo usaremos para determinar cuánto debe moverse a la derecha:

alien_0 = {"x_posicion" : 0, "y_posicion" : 25, "velocidad" : "rapida"}
print(f"posicion original : {alien_0['x_posicion']}")

# mover el alien a la derecha
# determina ahora la velocidad del alien vasado en su velocidad actual

if alien_0["velocidad"] == "lenta":
    x_incrementa = 1
elif alien_0["velocidad"] == "mediana":
    x_incrementa = 2
else : x_incrementa = 3
alien_0["velocidad"] == "rapida"
alien_0["x_posicion"] = alien_0["x_posicion"] + x_incrementa
print (f'nueva posicion: {alien_0["x_posicion"]}')
