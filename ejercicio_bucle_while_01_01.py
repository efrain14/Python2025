# Solución al ejercicio 7-4: Ingredientes de pizza
prompt = "\nPor favor, ingresa un ingrediente para tu pizza:"
prompt += "\n(Escribe 'salir' para terminar la orden) "

while True:
    ingredientes = input(prompt)
    
    if ingredientes.lower() == 'Salir':
        break
    else:
        print(f"¡Añadiré {ingredientes} a tu pizza!")

print("¡Gracias por tu pedido!")