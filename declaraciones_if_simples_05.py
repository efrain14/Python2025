"""crear una lista de ingredientes solicitados por el cliente y usando un bucle
para anunciar cada ingrediente a medida que se añade a la pizza:"""
ingredientes_adicionales = ["champiniones", "pepperoni", "mozarela", "aceitunas"]
for ingrediente_adicional in ingredientes_adicionales:
    print(f"Adicional {ingrediente_adicional}.")
print("\n has finalizado el pedido de tu pizza!")
# si la pizzeria se queda sin aceitunas se realiza una declaracion IF dentro del
# bucle FOR puede manejar la situacion
print("\n")
ingredientes_adicionales2 = ["pepperoni", "aceitunas", "mozarela"]
for ingrediente_adiciona1 in ingredientes_adicionales2:
    if ingrediente_adiciona1 == "aceitunas":
        print("lo sentimos hoy no contamos con aceitunas")
    else:
        print(f"Adicional {ingrediente_adiciona1}.")
print("\n has finalizado el pedido de tu pizza!")
print("\n")
ingredientes_adicionales = []
if ingredientes_adicionales:
    for ingrediente_adicional in ingredientes_adicionales:
        print(f"Adicional de {ingrediente_adicional}.")
    print("terminaste de hacer tu pedido")
else:
    print("estas seguro de querer una pizza simple?")
