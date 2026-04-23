"""MODIFICAR UNA LISTA EN UNA FUNCION 02
Cuando pasa una lista a una funcion, la funcion puede modificar la
lista. Cualquier cambio realizado en la lista dentro del cuerpo de la
funcion es permanente, lo que le permite trabajar de manera
eficiente incluso cuando maneja grandes cantidades de datos.
Considere una empresa que crea modelos impresos en 3D de
diseños que envian los usuarios. Los diseños que deben imprimirse
se almacenan en una lista y, una vez impresos, se mueven a una
lista separada. El siguiente codigo hace esto sin usar funciones:"""

# Comienza con algunos diseños que necesiten ser impresos.
unprinted_designs = ["case de cel", "vaso", "taza", "sello"]
completed_models = []

# Simula la impresión de cada diseño hasta que no quede ninguno.
# Mueve cada diseño a la sección de modelos completados después de imprimirlo.

while unprinted_designs :
    current_desings = unprinted_designs.pop()
    print(f"Modelos Impresos : {current_desings}")
    completed_models.append(current_desings)
    
# muestra todos los modelos completados
print("\nlos siguientes modelos fueron impresos:")
for completed_model in completed_models:
    print(completed_model)