"""codigo que genera automaticamente cada extraterrestre una flota de 30 alienigenas"""

aliens = []
# crea 30 aliens verdes
for numero_aliens in range(30):
    nuevo_alien = {"color" : "verde", "puntos" : 5, "velocidad" : "lenta"}
    aliens.append(nuevo_alien)
for alien in aliens[:5]:  #muestra los primeros 5 aliens
    print(alien)
print(f"numero total de aliens creados: {len(aliens)}")
