"""  ELIMINAR TODAS LAS INSTANCIAS DE VALORES ESPECIFICOS DE UNA LISTA
En el Capitulo 3, usamos remove() para eliminar un valor especifico
de una lista. La funciön remove() funcioné porque el valor que nos
interesaba apareciö solo una vez en la lista. Pero, qué sucede si
desea eliminar todas las instancias de un valor de una lista?
Supongamos que tiene una lista de mascotas con el valor 'gato'
repetido varias veces. Para eliminar todas las instancias de ese valor,
puede ejecutar un bucle while hasta que 'gato' ya no esté en la lista,
como se muestra aqui  """

mascotas = ["perro", "gato", "perro", "mono", "caballo", "gato", "conejo", "gato", "cerdo"]

print(mascotas)

while "gato" in mascotas:
    mascotas.remove("gato")
print(mascotas)    