""" PRUEBELO USTED MISMO   8-12  FUNCIONES  
Sándwiches: escriba una función que acepte una lista de elementos que una
persona quiere en un sándwich. La función debe tener un parámetro que recopile
tantos elementos como proporcione la llamada a la función y debe imprimir un
resumen del sándwich que se está pidiendo. Llame a la función tres veces, utilizando una cantidad diferente dea umentos cada vez."""

def hacer_sandwich(tamano, *ingredientes):
    """toma la orden del sandwich e imprime sus ingredientes"""
    print(f"Hacer el sandwich de tamaño: {tamano} y agregarle los siguientes ingredientes: ")
    for ingrediente in ingredientes:
        print(f" _ {ingrediente}")
        
hacer_sandwich("tamaño mediano", "lechuga", "tomate", "cebolla", "pepino", "queso cheddar", "jamon", "salami")

hacer_sandwich("tamaño pequeño", "lechuga", "pepinillos", "queso amarillo", "salami", "peperoni", "aceituna")

hacer_sandwich("tamaño extra grande", "queso gouda", "salami", "salchichon", "espinaca", "tomate", "huevo")