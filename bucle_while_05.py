""" USANDO CONTINUAR EN UN BUCLE 
En lugar de salir completamente de un bucle sin ejecutar el resto de
su cédigo, puede utilizar la instrucciån continue para volver al
principio del bucle, segün el resultado de una prueba condicional.
Por ejemplo, considere un bucle que cuenta del 1 al 10 pero imprime
solo los nümeros impares en ese rango:"""


cuenta_numeros = 0
while cuenta_numeros < 10 :
    cuenta_numeros += 1
    if cuenta_numeros % 2 == 0 :
        continue
    
    print(cuenta_numeros)
    
#     Primero, configuramos current_number en 0. Como es menor que 10, Python ingresa al bucle while. Una vez dentro del ciclo,  incrementamos el recuento en 1 por lo que
# current number es 1. La instrucciön if luego verifica el m6dulo de
# current _ number y 2. Si el m6dulo es 0 (lo que significa current_number es divisible por 2), la
# declaraciön continue le dice a Python que ignore el resto del bucle y
# volver al principio. Si el nümero actual no es divisible por 2, se
# ejecuta el resto del ciclo y Python imprime el nümero actual: