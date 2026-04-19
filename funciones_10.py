""" FUNCIONES hacer que un valor sea opcional 2 
Pero los segundos nombres no siempre son necesarios, y esta
funcion tal como estå escrita no funcionaria si intentara llamarla solo
con un nombre y un apellido. Para que el segundo nombre sea
opcional, podemos darle al argumento segundo_nombre un valor
predeterminado vacío e ignorar el argumento a menos que el
usuario proporcione un valor. Para que nombre_formateado()
funcione sin un segundo nombre, configuramos el valor
predeterminado de segundo_nombre en una cadena vacía y lo movemos
al final de la lista de parámetros:"""

def nombre_formateado(primer_nombre, apellido, segundo_nombre ="") :
    """funcion que formatea el nombre completo de un trabajador"""
    if segundo_nombre:
        nombre_completo = f"{primer_nombre} {segundo_nombre} {apellido}"
    else:
        nombre_completo = f"{primer_nombre} {apellido}"
    return nombre_completo.title()

trabajador = nombre_formateado("junior", "calderon")
print(trabajador)
trabajador = nombre_formateado("pedro", "briceño")
print(trabajador)
trabajador = nombre_formateado("efrain", "garcia", "jose")
print(trabajador)