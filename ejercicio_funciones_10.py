""" PRUEBELO USTED MISMO  8-9 
Mensajes: haga una lista que contenga una serie de mensajes de texto cortos.
Pase la lista a una funcion llamada show_messages(), que imprime cada mensaje de
texto."""

def show_messages(menssages):
    """muestra todos los mensajes de una lista"""
    for menssage in menssages:
        print(menssage)
        
menssages = ["Hola como estas", "nos vemos pronto"]
show_messages(menssages)
