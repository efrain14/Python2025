""" EVITAR QUE UNA FUNCION  MODIFIQUE UNA LISTA 
A veces querrás evitar que una función modifique una lista. Por
ejemplo, digamos que comienza con una lista de diseños no
impresos y escribe una función para moverlos a una lista de modelos
completados, como en el ejemplo anterior. Puede decidir que,
aunque haya impreso todos los diseños, desea conservar la lista
original de diseños no impresos para sus registros. Pero debido a
que sacó todos los nombres de diseños de disenos_porimprimir, la
lista ahora está vacía y la lista vacía es la única versión que tiene; el
original se ha ido. En este caso, puede solucionar este problema
pasando a la función una copia de la lista, no la original. Cualquier
cambio que la función realice en la lista afectará solo a la copia,
dejando intacta la lista original.
Puede enviar una copia de una lista a una funciön como esta:
function name (list name [ : ] )
La notaciön de segmento hace una copia de la lista para enviarla
a la funcion. Si no quisiéramos vaciar la lista de diseöos no impresos
en Printing_models.py, podriamos llamar a print_models
asi:
print models (unprinted designs [ : ] , completed models)"""

def print_models(unprinted_designs[:], completed_models):
    """simula la imprecion de cada diseno hasta que no quede ninguno, Tras la 
    impresión, mueve cada diseño a la sección de modelos terminados. """
    while unprinted_designs :
        current_design = unprinted_designs.pop()
        print(f"\nModelos Impresos: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """ mustratodos los modelos que se imprimieron"""
    print("\n los siguientes modelos se imprimieron: ")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ["case de cel", "vaso", "taza", "sello"]
completed_models = []
