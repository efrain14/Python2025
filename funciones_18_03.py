""" FUNCIONES 
Mezclando argumentos posicionales y arbitrarios
Si desea que una funci6n acepte varios tipos diferentes de argumentos, el 
paråmetro que acepta un nümero arbitrario de argumentos debe colocarse al final
en la definiciön de la funciön. Python primero compara los argumentos posicionales
y de palabras clave y luego recopila los argumentos restantes en el paråmetro
final. Por ejemplo, si la funci6n necesita tomar un tamaño para la pizza,
ese paråmetro debe ir antes del paråmetro *toppings:"""

def hacer_pizza(tamano, *toppings):
    """imprime el tamaño y los toppings que llevara la pizza"""
    print(f"\nhacer la pizza de tamaño {tamano} con los siguientes ingredientes: ")
    for topping in toppings:
        print(f"- {topping}")
hacer_pizza("extra familiar", "champiñones", "aceitunas", "salami", "extra de queso")
hacer_pizza("normal", "peperoni")