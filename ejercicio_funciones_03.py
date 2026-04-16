""" PRUEBELO USTED MISMO  8-3 
Camiseta: Escribe una funciån llamada elabora_camiseta() que acepte una talla y el texto de un mensaje que debe imprimirse en la camiseta. La funciån debe imprimir una oraciån que resuma el tamaäo de la camiseta y el mensaje impreso en ella.
Llame a la funci6n una vez usando argumentos para hacer una camisa.
Llame a la funciån segunda vez utilizando argumentos de palabras clave."""

def elabora_camiseta(talla, texto) :
    """muestra la talla y una oracion de una camiseta"""
    
    print(f"\nla talla de la camisa es {talla}")
    print(f"el texto que llevara la camiseta es {texto}")
elabora_camiseta(talla= "Media", texto= "'i love python'")