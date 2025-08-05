""""usando la funcion range()"""
for valor in range(1, 5):
    print(valor)
for valor in range(1, 6):
    print(valor)
for valor in range(6):
    print(valor)
numeros = list(range(1, 6))
print(numeros)
numeros_pares = list(range(2, 11, 2))
print(numeros_pares)
#Comenzamos con una lista vacía llamada cuadrados. Luego, le indicamos a Python que
# recorra cada valor del 1 al 10 usando la función range(). Dentro del bucle, el valor
# actual se eleva a la segunda potencia y se asigna a la variable cuadrado 1.
# Cada nuevo valor de cuadrado se añade a la lista cuadrados 2. Finalmente, al finalizar el
# bucle, se imprime la lista de cuadrados."""
cuadrados = []
for valor in range(1, 11):
    cuadrado = valor ** 2
    cuadrados.append(cuadrado)
print(cuadrados)
#"para escribir este codigo de manera mas concisa, omita la variable temporal cuadrado y
# agregue cada valor nuevo directamente a la lista
cuadrados = []
for valor in range(1, 11):
    cuadrados.append(valor**2)
    print(cuadrados)
#Algunas funciones de Python son útiles al trabajar con listas de números. Por ejemplo, puedes
# encontrar fácilmente el mínimo, el máximo y la suma de una lista de números:
digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digitos))
print(max(digitos))
print(sum(digitos))
#El siguiente ejemplo crea la misma lista de numeros cuadrados que vio anteriormente,
# pero utiliza una lista por comprecion
print("\n")
cuadrados = [valor**2 for valor in range(1, 11)]
print(cuadrados)
