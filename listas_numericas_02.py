"""4-3. Contar hasta veinte: Usa un bucle for para imprimir los números del 1 al 20,
ambos inclusive.
4-4. Un millón: Crea una lista de los números del uno al millón y luego usa un bucle
for para imprimirlos. (Si la salida tarda demasiado, deténla presionando CTRL-C o
cerrando la ventana de salida).
4-5. Sumar un millón: Crea una lista de los números del uno al millón y luego usa min()
y max() para asegurarte de que la lista comience en uno y termine en un millón. También
usa la función sum() para ver qué tan rápido Python puede sumar un millón de números.
4-6. Números impares: Usa el tercer argumento de la función range() para crear una lista
de los números impares del 1 al 20. Usa un bucle for para imprimir cada número.
4-7. Tres: Haz una lista de los múltiplos de 3, del 3 al 30. Usa un bucle for para
imprimir los números de tu lista.
4-8. Cubos: Un número elevado a la tercera potencia se llama cubo. Por ejemplo, el cubo de
2 se escribe 2**3 en Python. Haz una lista de los primeros 10 cubos
(es decir, el cubo de cada entero del 1 al 10) y usa un bucle for para imprimir el valor de cada
cubo.
4-9. Comprensión de cubos: Usa una comprensión de listas para generar una lista de los primeros
10 cubos."""
for valor in range(1, 21):
    print(valor)
print("\n")
# for valor in range(1, 1000_001):
#     print(valor)
# print("\n")
# numeros = list(range(1, 1_000_001))
# minimo = min(numeros)
# maximo = max(numeros)
# suma = sum(numeros)
# print("el numero minimo es ",minimo,"el numero maximo es el ",maximo,"y la suma da ",suma)
print("\n")
for numeros in range(1, 21, 2):
    print(numeros)
print("\n")
multiplos_de_3 = list(range(3, 31, 3))
print(multiplos_de_3)
print("\n")
cubos = []
for valor in range(1, 11):
    cubo = valor**3
    cubos.append(cubo)
    print(cubo)
print("\n")
cubos = [valor ** 3 for valor in range(1, 11)]
print(cubos)
