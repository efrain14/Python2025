"""Listas numericas"""
jugadores = ["carlos", "miguel", "luis", "juan", "pedro"]
print(jugadores[0:3])
print(jugadores[1:4])
print(jugadores[:4])
print(jugadores[:])
print(jugadores[2:])
print(jugadores[-3:])
print("\n")
print("Estos son los primeros tres jugadores de mi equipo:")
for jugador in jugadores[:3]:
    print(jugador.title())
