"""                PRUEBELO USTED MISMO 6-3
Glosario: use cinco palabras de programacion como claves y use su significado
como valores, imprima cada palabra y su significado como resultado cidadosamente
formateado puede imprimir la palabra seguida de dos puntos y luego su 
significado, o imprimir """

glosario = {
"algoritmo" : "es un conjunto de pasos para una determinada tarea",
"codigo" : "conjunto de palabras o simbolos que contienen instrucciones para la PC",
"codigo maquina" : "codigo que la PC puede entender y ejecutar"    
}
descripcion = glosario["codigo"].title()
print(f'el termino codigo em programacion significa: {descripcion}.')