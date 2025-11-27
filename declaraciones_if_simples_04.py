""""pruebelo usted mismo 5-3 al 5-6  alien_color"""
color_alien = "verde"
if color_alien == "verde":
    print("acabas de ganar 5 Ptos.")
color_alien = "verde"
if color_alien == "rojo":
    print("acabas de ganar 5 Ptos.")
else:
    print("acabas de ganar 10 Ptos.")
print("\n")
color_alien = "rojo"
if color_alien == "verde":
    print("acabas de ganar 5 Ptos.")
elif color_alien == "amarillo":
    print("acabas de ganar 15 Ptos.")
else:
    print("acabas de ganar 10 Ptos.")
print("\n")
edad = 15
if edad < 2:
    print("la persona es un bebe")
elif edad >= 2 and edad <= 4:
    print("la persona es un niño pequeño")
elif edad > 4 and edad <= 13:
    print("la persona es un niño")
elif edad > 13 and edad <= 20:
    print("la persona es un adolecente")
elif edad > 20 and edad <= 65:
    print("la persona es un adulto")
else:
    print("la persona es una persona mayor")
