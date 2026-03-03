"""USAR BREAK  PARA SALIR DE UN BUCLE 
Para salir de un bucle while inmediatamente sin ejecutar ningün
cédigo restante en el bucle, independientemente de los resultados
de cualquier prueba condicional, utilice la instrucci6n break. La
declaraciön break dirige el flujo de su programa; puede usarlo para
controlar qué lineas de cédigo se ejecutan y cuåles no, de modo que
el programa solo ejecute el cédigo que usted desee, cuando asi 1o
desee. Por ejemplo, considere un programa que pregunta al usuario sobre los lugares que ha visitado. Podemos detener el bucle while en este programa llamando a break tan pronto como el usuario ingrese el valor quit' :"""

prompt = "\npor favor ingrse el nombre de una ciudad que usted halla visitado:"
prompt += "\n escriba salir cuando halla terminado."

while True :
    ciudad = input(prompt)
    
    if ciudad == "salir" :
        break
    else :
        print(f"yo adoro ir a {ciudad.title()} !")