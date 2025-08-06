"""parque_de_atarcciones.py"""
# la entrada para cualquier menor de 4 años es gratuita
# la entrada para cualquiera persona entre 4 y 18 años es de $ 25
# la entrada para todos los mayores de 18 años es de $ 40
edad = 22
if edad < 4:
    print("el costo de tu entrada es $ 0")
elif edad < 18:
    print("el costo de tu entrada es $ 25")
else:
    print("el costo de tu entrada es $ 40")

# en lugar de imprimir el precio de entrada dentro del bloque IF-ELIF-ELSE
# seria mas conciso establecer solo el precio dentro del bloque IF-ELIF-ELSE
# cadena y luego tener una unica llamada PRINT() que se ejecute de que la cadena 
# ha sido evaluada
print("\n")
edad = 67
if edad < 4:
    precio = 0
elif edad < 18:
    precio = 25
elif edad < 65:
    precio = 40
else:
    precio = 20
print(f"tu costo de entrada es de ${precio}.")
