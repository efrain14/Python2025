"""Usar multiples listas """
# El siguiente ejemplo define dos listas. La primera es la lista de ingredientes disponibles en la pizzería y la segunda, la lista de ingredientes solicitados por el usuario. En esta ocasión, cada elemento de la lista de ingredientes solicitados se compara con la lista de ingredientes disponibles antes de añadirlo a la pizza:

adicionales_disponibles = ["cebolla", "pepperoni", "mozarela", "parmesano", "campinones", "aceitunas"]
adicionales_pedidos = ["cebolla", "mozarela", "jamon", "aceitunas"]
for adicional_pedido in adicionales_pedidos:
    if adicional_pedido in adicionales_disponibles:
        print(f"Adicionales {adicional_pedido}.")
    else:
        print(f"lo sentimos no contamos con {adicional_pedido}.")
print("hemos terminado con su pedido")
