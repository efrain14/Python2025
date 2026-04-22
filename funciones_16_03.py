""" FUNCIONES VIENE DE EL CODIGO ANTERIRO 
Podemos reorganizar este código escribiendo dos funciones, cada
una de las cuales realiza un trabajo específico. La mayor parte del
código no cambiará; simplemente lo estamos estructurando con más
cuidado. La primera función se encargará de imprimir los diseños y
la segunda resumirá las impresiones que se han realizado:"""

def modelos_imprecion(disenos_porimprimir, modelo_completo):
    """simula la imprecion de cada diseno hasta que no quede ninguno, Tras la impresión, mueve cada diseño a la sección de modelos terminados. """
    while disenos_porimprimir :
        diseno_actual = disenos_porimprimir.pop()
        print("\nModelos Impresos : {diseno_actual}")
        
def mustra_modelocompleto(modelo_completo):
    """ mustratodos los modelos que se imprimieron"""
    print("\n los siguientes modelos se imprimieron: ")
    for modelo_completos in modelo_completo:
        print(modelo_completo)
diseno_porimprimir = ["case de cel", "vaso", "taza", "sello"]
modelo_completo = []

modelos_imprecion(diseno_porimprimir, modelo_completo)
mustra_modelocompleto(modelo_completo)
