"""" 
3-8. Viendo el mundo: Piensa en al menos cinco lugares del mundo que te gustaría visitar.

Guarda las ubicaciones en una lista. Asegúrate de que la lista no esté en orden alfabético.

Imprime la lista en su orden original. No te preocupes por imprimirla correctamente; simplemente imprímela como una lista de Python sin formato.

Usa sorted() para imprimir la lista en orden alfabético sin modificar la lista original.

Muestra que la lista sigue en su orden original imprimiéndola.

Usa sorted() para imprimir la lista en orden alfabético inverso sin cambiar el orden de la lista original.

Muestra que la lista sigue en su orden original imprimiéndola de nuevo.

Usa reverse() para cambiar el orden de la lista. Imprime la lista para mostrar que su orden ha cambiado.

Usa reverse() para cambiar el orden de la lista de nuevo. Imprime la lista para mostrar que ha vuelto a su orden original.
• Usa sort() para cambiar tu lista y que se guarde en orden alfabético. Imprime la lista para indicar que se ha cambiado el orden.
• Usa sort() para cambiar tu lista y que se guarde en orden alfabético inverso. Imprime la lista para indicar que se ha cambiado el orden.

3-9. Invitados a cenar: Trabajando con uno de los programas de los ejercicios 3-4 a 3-7 (páginas 41-42), usa len() para imprimir un mensaje que indique el número de personas a las que invitas a cenar.

3-10. Función Every: Piensa en cosas que podrías almacenar en una lista. Por ejemplo, podrías crear una lista de montañas, ríos, países, ciudades, idiomas o cualquier otra cosa que desees. Escribe un programa que cree una lista con estos elementos y luego utilice cada función presentada en este capítulo al menos una vez.
"""
lugares = ["japon", "grecia", "australia", "maldivas", "suisa", "singapur"]
print(lugares)
print(sorted(lugares))
print(lugares)
lugares_decendente = sorted(lugares)
print(lugares_decendente)
print(lugares)
lugares_acendentes = sorted(lugares, reverse=True)
print(lugares_decendente)
sorted(lugares,reverse=True)
print(lugares)
lugares.sort()
print(lugares)
lugares.sort(reverse=True)
print(lugares)
print("\n")
lista_invitados = ["luis", "carlet"]
len(lista_invitados)
print(len(lista_invitados))
print(f"vamos a invitar a {(len(lista_invitados))} personas a la cena de gala de esta noche")
print(lugares [-1])