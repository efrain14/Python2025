"""Numeros ordinales"""
#Los números ordinales indican su posición en una lista, como 1.º o 2.º. La
# mayoría de los números ordinales terminan en th , excepto 1, 2 y 3.

#Almacene los números del 1 al 9 en una lista.
#Recorrer la lista.
#Utilice una if-elif-else cadena dentro del bucle para imprimir la terminación
# ordinal correcta de cada número. La salida #debe ser "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", y cada resultado debe estar en una línea aparte.
numeros = list(range(1,10))
for numero in numeros:
    if numero == 1:
        print("1st")
    elif numero == 2:
        print("2nd")
    elif numero == 3:
        print("3rd")
    else:
        print(f"{numero}th")