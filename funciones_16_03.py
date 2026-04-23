""" FUNCIONES VIENE DE EL CODIGO ANTERIRO 
Podemos reorganizar este código escribiendo dos funciones, cada
una de las cuales realiza un trabajo específico. La mayor parte del
código no cambiará; simplemente lo estamos estructurando con más
cuidado. La primera función se encargará de imprimir los diseños y
la segunda resumirá las impresiones que se han realizado:"""

def print_models(unprinted_designs, completed_models):
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

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
