""" PRUEBELO USTED MISMO   FUNCIONES  8-10 
Envío de mensajes: comience con una copia de su programa del Ejercicio 8-9.
Escriba una función llamada send_messages que imprima cada mensaje de texto y
mueva cada mensaje a una nueva lista llamada sent_messages a medida que se
imprime. Después de llamar a la función, imprima ambas listas para asegurarse de que los mensajes se movieron correctamente."""

def show_messages(messages):
    """muestra todos los mensajes de una lista"""
    for message in messages:
        print(message)
        



def send_messages(messages, sent_messages):
    """envia los mensajes de la lista"""
    print("\nMuestra todos los mensajes")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["Hola como estas", "nos vemos pronto"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\n Lista Final")
print(messages)
print(sent_messages)