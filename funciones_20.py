""" FUNCIONES ALMACENAMIENTO DE FUNCIONES EN MODULOS 
Importar un módulo completo
Para comenzar a importar funciones, primero necesitamos crear un
módulo. Un módulo es un archivo que termina en .py y que contiene
el código que desea importar a su programa. Hagamos un módulo
que contenga la función hacer_pizza()
Para crear este módulo, eliminaremos todo del archivo hacer_pizza.py excepto la función"""

def hacer_pizza(tamano, *toppings):
    """agrga los ingredientes y el tamaño de una pizza"""
    print(f"\nhacer la pizza de tamaño {tamano} con los siguientes ingredientes:")
    for topping in toppings:
        print(f"- {topping}")
        
# Ahora crearemos un archivo separado llamado hecer_pizzas.py en
# el mismo directorio que pizza.py. Este archivo importa el módulo que acabamos de crear y luego realiza dos llamadas a hecer_pizza():

