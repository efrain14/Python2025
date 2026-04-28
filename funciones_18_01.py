""" FUNCIONES 
Pasar un número arbitrario de argumentos
A veces no sabrá de antemano cuántos argumentos debe aceptar una función. 
Afortunadamente, Python permite que una función recopile una cantidad arbitraria
de argumentos de la declaración de llamada.
Por ejemplo, considere una función que construye una pizza. Debe aceptar una 
cantidad de ingredientes, pero no se puede saber de antemano cuántos ingredientes
querrá una persona. La función en el siguiente ejemplo tiene un parámetro, 
*toppings, pero este parámetro recopila tantos argumentos como proporciona la 
línea de llamada:"""

#  PIZZA.PY
def hacer_pizza(*toppings):
    """imprime el listado de toppings que son requeridos"""
    print(toppings)
hacer_pizza("peperoni")
hacer_pizza("chanpiñones", "tomate", "salami", "extra de queso", "aceitunas")