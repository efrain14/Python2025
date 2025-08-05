"""4-2. Animales: Piensa en al menos tres animales diferentes que tengan una característica 
común. Guarda los nombres de estos animales en una lista y luego usa un bucle for para imprimir 
el nombre de cada animal.
• Modifica tu programa para imprimir una declaración sobre cada animal, como 
"Un perro sería una excelente mascota".
• Agrega una línea al final del programa que indique qué tienen en común estos animales. 
Podrías imprimir una oración como "Cualquiera de estos animales sería una excelente mascota"."""

animales = ["gato","perro", "conejo", "tortuga"]
for animal in animales:
    print(animal.title())

for animal in animales:
    print("Un "f"{animal.title()} seria una excelente mascota")

print("todos estos animales son pequeños \ny son excelentes mascotas")
