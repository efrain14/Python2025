"""               UNA LISTA EN UN DICCIONARIO
En lugar de poner un diccionario dentro de una lista, a veces resulta
útil poner una lista dentro de un diccionario. Por ejemplo, considere
cómo describiría una pizza que alguien está pidiendo. Si usaras solo
una lista, todo lo que realmente podrías almacenar es una lista de
los ingredientes de la pizza. Con un diccionario, una lista de
ingredientes puede ser sólo un aspecto de la pizza que estás
describiendo.
En el siguiente ejemplo, se almacenan dos tipos de información para
cada pizza: un tipo de corteza y una lista de ingredientes. La lista de
ingredientes es un valor asociado con la clave 'toppings'. Para usar
los elementos de la lista, damos el nombre del diccionario y la clave
toppings, como lo haríamos con cualquier valor del diccionario. En
lugar de devolver un valor único, obtenemos una lista de ingredientes:"""

# Tienda informacion de las pizzas ordenadas
pizza = {
        "masa" : "gruesa",
        "toppings" : ["champinones", "extra de queso"],
}

#finalisa el pedido
print(f"tu ordenaste una pizza de maza {pizza['masa']} "
    " con los siguientes topping:")

for topping in pizza ["toppings"]:
    print(f"\t{topping}")