"""LLENAR UN DICCIONARIO CON ENTRADAS DEL USUARIO 
Puede solicitar tanta entrada como necesite en cada paso a través
de un bucle while. Hagamos un programa de encuesta en el que
cada paso por el bucle solicite el nombre y la respuesta del
participante. Almacenaremos los datos que recopilamos en un
diccionario, porque queremos conectar cada respuesta con un
usuario en particular:"""

respuestas = {}
# establece una bandera para indicar que la encuesta esta activa
encuesta_activa = True

while encuesta_activa :
    # mientras la encuesta este activa, Solicita el nombre y la respuesta de la persona
    nombre = input("\nCual es tu Nombre? ")
    respuesta = input("Que montaña te gustaria escalar algun dia?")
    #almacena la respuesta en el diccionario
    respuestas[nombre] = respuesta
    
    # averigua si alguien mas va a participar en la encuesta
    repetir = input("te gustaria que otra persona respondiera (si/no) ")
    if repetir == "no" :
        encuesta_activa = False
        
# la encuesta esta completa. y muestra el resultado
print("\n--- resultados de la encuesta ---")
for nombre, respuesta in respuestas.items() :
    print(f"{nombre} le gustaria escalar {respuesta}. ")        
    