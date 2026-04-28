""" PRUEBELO USTED MISMO  FUNCIONES  8-11 8-11. Mensajes archivados: comience con 
su trabajo del Ejercicio 8-10. Llame a la funcion send_messages o con una copia de
la lista de mensajes. Después de llamar a la funciön, imprima ambas listas para
mostrar que la lista original ha conservado sus mensages."""

def show_messages(messages):
    """muestra todos los mensajes de una lista"""
    print("Muestra todos los mensages")
    for message in messages:
        print(message)
        



def send_messages(messages, sent_messages):
    """ imprime los mensages y los mueve a sent_meessages"""
    print("\nEnvia todos los mensajes")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["Hola como estas", "nos vemos pronto", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\n Lista Final")
print(messages)
print(sent_messages)