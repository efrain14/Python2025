""" 7-3. Mültiplos de diez: solicite al usuario un nümero y luego informe si el nümero es mültiplo de 10 0 no."""

numero = input("por favor escriba un numero ")
numero = int(numero)
if numero  % 10 == 0 :
    print(f"\nel numero {numero} es multiplo de 10")
else :
    print(f"\nel numero {numero} no es multiplo de 10")