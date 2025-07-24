# modificacion de elementos de una lista
motos = ["yamaha", "honda", "suzuky", "bmw", "bera"]
autos = []
print(motos)
motos[0] = "ducati"
print(motos)
motos[-1] = "yamaha"
print(motos)
motos.append("bears")   #mediante el metodo append se agrega un nuevo elemento a la lista
print(motos)
autos.append("ford")
autos.append("renaul")
autos.append("fiat")
autos.append("volvo")
print(autos)
autos.insert(0,"mercedes")
print(autos)
autos.insert(5, "toyota")
print(autos)
del autos[1]
print(autos)
pop_autos = autos.pop()
print(autos)
print(pop_autos)
ultimo_adquirido = autos.pop()
print(f"el ultimo auto que adquiri fue un {ultimo_adquirido.title()}.")
autos.remove("renaul")
print(autos)
autos.insert(0, "volvo")
autos.insert(1, "toyota")
autos.insert(2, "ford")
print(autos)
demasiado_caro = "mercedes"
autos.remove(demasiado_caro)
print(autos)
print(f"\nEl {demasiado_caro.title()} es demaciado caro para mi")