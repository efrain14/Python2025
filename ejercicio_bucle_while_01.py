"""               7-4. Ingredientes para pizza: 
escriba un bucle que solicite al usuario que ingrese una serie de ingredientes para pizza hasta que ingrese un valor . A medida que ingresan cada ingrediente, imprima un mensaje que indique que agregará ese ingrediente a su pizza."""

prompt = "\nIngrese un ingrediente de la pizza:  "

prompt += "\nEscriba Salir para terminar la orden "

while  True:
    ingredientes = input(prompt)
    
    if ingredientes.lower() == "Salir":
        break
    else:
        print(f"Vas a agrgarle {ingredientes} a tu pizza ")
        
print("Gracias por tu pedido")