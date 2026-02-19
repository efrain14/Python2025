""" 7-2. Asientos en restaurante: escriba un programa que pregunte al usuario cuåntas personas hay en su grupo para cenar. Si la respuesta es mås de ocho, imprima un mensaje diciendo que tendrån que esperar por una mesa. En can contrario, informe que su mesa estå lista."""

comensales = input("Buenas, cuantos personas van a venir a cenar ")
comensales = int(comensales)

if comensales > 8 :
    print("lo sentimos tendran que esperar unos minutos mas por una mesa")
else :
    print("su mesa esta lista, pasen adelante")
    