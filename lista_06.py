""""3-7. Reducción de la lista de invitados: Acabas de descubrir que tu nueva mesa no llegará a tiempo para la cena y ahora solo tienes espacio para dos personas.
• Comienza con el programa del Ejercicio 3-6. Agrega una nueva línea que imprima un mensaje indicando que solo puedes invitar a dos personas a cenar.
• Usa pop() para eliminar invitados de tu lista, uno a la vez, hasta que solo queden dos nombres. Cada vez que extraigas un nombre de la lista, imprime un mensaje para esa persona, diciéndole que lamentas no poder invitarla a cenar.
• Imprime un mensaje para cada una de las dos personas que aún están en tu lista, informándoles de que siguen invitadas.
• Usa del para eliminar los dos últimos nombres de tu lista, de modo que tengas una lista vacía. Imprime la lista para asegurarte de que esté vacía al final del programa."""

lista_invitados = ['ersy', 'efrain', 'maria', 'luis', 'junior', 'alexis', 'jose', 'carlet']
print("lamentamos informarles que devido a causas de fuerza mayor\n no podremos albergar a todos los invitados \n por lo tanto pasaremos cartas explicando la anulacion de la invitacion")
lamento = "lamentamos tener que suspender su invitacion para esta noche"
s1 = "señor"
s2 = "señora"
print("\n")
print(s2,f"{lista_invitados.pop(0)} {lamento.title()}")
print("\n")
print(s1,f"{lista_invitados.pop(1)} {lamento.title()}")
print("\n")
print(s2,f"{lista_invitados.pop(2)} {lamento.title()}")
print("\n")
print(s1,f"{lista_invitados.pop(3)} {lamento.title()}")
print("\n")
print(s1,f"{lista_invitados.pop(0)} {lamento.title()}")
print("\n")
print(s1,f"{lista_invitados.pop(1)} {lamento.title()}")
print("\n")
print(lista_invitados)
print(s1,f"{lista_invitados[0]}"+" usted continua invitado para esta noche")
print(s2,f"{lista_invitados[1]}"+" usted continua invitado para esta noche")
del lista_invitados[1]
del lista_invitados[0]
print(lista_invitados)