""" PRUEBELO USTED MISMO 7-9 
sin pastrami utilizando la lista orden_sandwich del ejercicio 7-8 asegurese de que el sandwich 'pastrami' aparesca en la lista al menos 3 veces. Agregue codigo cerca del comienzo de su programa para imprimir un mensaje que indique que la tienda se ha quedado sin pastrami y luego use un bucle while para eliminar todas las apariciones de pastrami de orde_sandwich asegurece de que ningun sandwiche de pastrami acabe en sandwiches_finalizados """

orden_sandwich = ["pepino", "pastrami", "atun", "albondigas","pastrami", "vegetariano", "jamon con queso", "peperoni", "pastrami"]
print(orden_sandwich)
print("\n")
print("Apreciados clientes lamntamos anunciar que nos hemos quedado sin pastrami")

while "pastrami" in orden_sandwich :
    orden_sandwich.remove("pastrami")
print(orden_sandwich)