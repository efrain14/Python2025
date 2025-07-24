autos = ["bmw","volvo", "ford","mercedes", "fiat","toyota", "chebrolet"]
print(autos)
autos.sort()    # con el metodo .sort() se ordena la lista alfabeticamente de forma permanente
print(autos)
autos.sort(reverse=True)
print(autos)    # con el metodo .sort() y el argumento reverse=True la lista se ordena en orden inverso al alfabeto
print("\n")
print("esta es la lista original; antes de ordenarla con la funcion 'sorted'")
print(autos)
print("\n esta es la lista ordenada con la funcion sorted")
print(sorted(autos))
print("esta es nuevamente la lista ordenada original")
print(autos)
print("\n")
autos.reverse()
print(autos)
print(len(autos))       # la funcion len muestra la longitud de una lista