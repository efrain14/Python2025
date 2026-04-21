"""MODIFICAR UNA LISTA EN UNA FUNCION 
Cuando pasa una lista a una funcion, la funcion puede modificar la
lista. Cualquier cambio realizado en la lista dentro del cuerpo de la
funcion es permanente, lo que le permite trabajar de manera
eficiente incluso cuando maneja grandes cantidades de datos.
Considere una empresa que crea modelos impresos en 3D de
diseños que envian los usuarios. Los diseños que deben imprimirse
se almacenan en una lista y, una vez impresos, se mueven a una
lista separada. El siguiente codigo hace esto sin usar funciones:"""

# Comienza con algunos diseños que necesiten ser impresos.
disenos_porimprimir = ["case de cel", "vaso", "taza", "sello"]
modelos_completos = []

# Simula la impresión de cada diseño hasta que no quede ninguno.
# Mueve cada diseño a la sección de modelos completados después de imprimirlo.

while disenos_porimprimir :
    diseno_actual = disenos_porimprimir.pop()
    print(f"Modelos Impresos : {diseno_actual}")
    modelos_completos.append(diseno_actual)
    
# muestra todos los modelos completados
print("\nlos siguientes modelos fueron impresos:")
for modelos_completo in modelos_completos:
    print(modelos_completo)