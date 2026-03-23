""" BUCLE WHILE USANDO UNA BANDERA 
En el ejemplo anterior, hicimos que el programa realizara ciertas tareas mientras una condición determinada era verdadera. Pero ¿qué pasa con los programas más  complicados en los que muchos eventos diferentes podrían provocar que el programa  deje deejecutarse? Por ejemplo, en un juego, varios eventos diferentes pueden  finalizar el juego. Cuando el jugador se queda sin barcos, se le acaba el tiempo o las ciudades que se suponía que debían proteger son destruidas, el juego debería terminar. Debe terminar si ocurre alguno de estos eventos. Si pueden ocurrir muchos
eventos posibles para detener el programa, intentar probar todas estas condiciones en una declaración while se vuelve complicado y difícil. Para un programa que debe ejecutarse sólo mientras se cumplan muchas condiciones, puede definir una variable  que determine si todo el programa está activo o no. Esta variable, llamada bandera,
actúa como una señal para el programa. Podemos escribir nuestros programas para que se ejecuten mientras el indicador esté establecido en True y dejen de ejecutarse cuando cualquiera de varios eventos establezca el valor del indicador en False.  Como resultado, nuestra declaraci6n general while necesita verificar solo una 
condiciön: si la bandera es actualmente TRUE Luego, todas nuestras Otras pruebas  (para ver si ocurriö un evento que deberia establecer el indicador en False) se pueden organizar claramente en el resto del programa.
Agreguemos una bandera a parrot.py de la secci6n anterior. Este
indicador, al que llamaremos ACTIVE (aunque puedes llamarlo como
quieras), controlarå si el programa debe continuar ejecutåndose o
no:"""


prompt = "\nDime algo y te lo repetire: "
prompt += "\n Ingrese 'salir' para finalizar el programa. "
active = True
while active :
    mensaje = input(prompt)
    if mensaje == "salir" :
        active = False
    else:
        print(mensaje)
        
        
#  Este programa tiene el mismo resultado que el ejemplo anterior
# donde colocamos la prueba condicional directamente en la
# declaraciön while. Pero ahora que tenemos una bandera para indicar
# si el programa general estå en un estado activo, seria fåcil agregar
# mås pruebas (como declaraciones elif) para eventos que deberian
# hacer que active se convierta en False. Esto es ütil en programas
# complicados como juegos, en los que puede haber muchos eventos
# que deberian hacer que el programa deje de ejecutarse. Cuando
# cualquiera de estos eventos hace que la bandera activa se convierta
# en False, se cerrarå el bucle principal del juego, se mostrarå un
# mensaje de Game Over y se le podrå dar al jugador la opci6n de
# jugar nuevamente."""