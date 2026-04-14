""" ejercicio 7-8 
Deli: has una lista llamada orden_sandwich  y rellenala con los nombres de varios ssndwiches. luego crea la lista vacia llamada sandwiches_finalisado  recorre la lista de pediidos de sandwiches e imprime un mensaje de cada pedido, como prepare tu sandwich de atun  A medida que se prepara cada shandwich, muevelo a la lista de sandwiches terminados. despues de que se hayan preparado todos los sandwches, imprima un mensaje enumerando cada sandwich que se preparo """

orden_sandwich = ["pepino", "atun", "albondigas", "vegetariano", "jamon con queso", "peperoni", "pastrami"]

sandwiches_finalizado = []

while orden_sandwich :
    sandwiches_en_preparacion = orden_sandwich.pop()
    print(f"estamos preparando tu Sandwiche de:  {sandwiches_en_preparacion.title()}")
    sandwiches_finalizado.append(sandwiches_en_preparacion)
print("\nSe han preparado los siguientes Sandwiches:")
for sandwiches_finalizado in sandwiches_finalizado :
    print(f"Sandwich de {sandwiches_finalizado}")