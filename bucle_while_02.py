""" PERMITIR QUE EL USUARIO ELEIJA CUANDO SALIR 
Podemos hacer que el programa parrot.py se ejecute todo el tiempo
que el usuario quiera poniendo la mayor parte del programa dentro
de un bucle while. Definiremos un valor de salida y luego
mantendremos el programa ejecutåpd—mientras el usuario no
haya ingresado el valor de salida:"""

prompt = "\nDime algo y te lo repetire: "
prompt += "\n Ingrese 'salir' para finalizar el programa. "
mensaje = ""
while mensaje != 'salir' :
    mensaje = input(prompt)
    print(mensaje)