"""PRUEBELO USTED MISMO  FUNCIONES  8-4 
Camisas grandes: modifique la funcion elabore_camiseta() para que las camisas sean grandes por defecto con un mensaje que diga Me encanta Python. Haz una camiseta grande y una camiseta mediana con el mensaje predeterminado, y una camiseta de cualquier talla con un mensaje diferente."""
def elabore_camisetas(talla, texto) :
    """funcion para mostrar la talla de camisetas y la frase escrita en ellas"""

    print(f"\nLa talla de las camiseta es {talla}")
    print(f"\nLa frase que se dibujara en la camiseta es: {texto}")
elabore_camisetas(talla = "Grande" , texto = "Me encanta Python")
elabore_camisetas(talla = "Mediana" , texto = "Me encanta Python")
elabore_camisetas(talla = "peqeña" , texto = "Me gusta programar en Python")