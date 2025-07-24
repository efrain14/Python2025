""""3-5. Cambio de la lista de invitados: Acabas de saber que uno de tus invitados no podrá asistir a la cena, así que necesitas enviar un nuevo conjunto de invitaciones. Tendrás que pensar en alguien más a quien invitar.
• Comienza con el programa del Ejercicio 3-4. Agrega una llamada a print() al final del programa, indicando el nombre del invitado que no podrá asistir.
• Modifica tu lista, reemplazando el nombre del invitado que no podrá asistir con el nombre de la nueva persona a la que invitas.
• Imprime un segundo conjunto de mensajes de invitación, uno para cada persona que aún esté en tu lista."""

lista_invitados = ["luis", "junior", "david", "alexis", "jose", "richard"]
print(lista_invitados)
invitado_ausente = lista_invitados.pop()
print(f"el señor {lista_invitados.pop(2)} no podra asistir esta noche")  # eliminamos a david de la lista
lista_invitados.insert(0, "efrain")
print(f"el señor,{lista_invitados[0]} es el nuevo invitado")
print(lista_invitados)
invitacion = " usted esta cordialmente invitado para la cena de esta noche "
print("señor",lista_invitados[0],invitacion )
print("señor",lista_invitados[1],invitacion )
print("señor",lista_invitados[2],invitacion )
print("señor",lista_invitados[3],invitacion )
print("señor",lista_invitados[4],invitacion )

