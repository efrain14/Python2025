""" FUNCIONES 
El asterisco en el nombre del parámetro *toppings le dice a Python que cree una
tupla llamada toppings, que contenga todos los valores que recibe esta función.
La llamada print() en el cuerpo de la función produce una salida que muestra que 
Python puede manejar una llamada a una función con un valor y una llamada con tres
valores. Trata las diferentes llamadas de manera similar. Tenga en cuenta que 
Python empaqueta los argumentos en una tupla, incluso si la función recibe solo
un valor: Ahora podemos reemplazar la llamada print() con un bucle que
recorre la lista de ingredientes y describe la pizza que se pide:"""

#  PIZZA.PY
def hacer_pizza(*toppings):
    """imprime el listado de toppings que son requeridos"""
    print("\nHacer la pizza con los siguientes ingredientes:")
    for topping in toppings:
        print(f"- {topping}")
hacer_pizza("peperoni")
hacer_pizza("chanpiñones", "tomate", "salami", "extra de queso", "aceitunas")