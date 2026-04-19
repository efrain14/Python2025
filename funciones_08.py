"""VALORES DE RETORNO  Devolver un valor simple,
veamos una funcion que toma un nombre y apellido y devuelve un nombre completo perfectamente formateado """

def nombre_formateado(primer_nombre, apellido) :
    """funcion que formatea un nombre completo"""
    nombre_completo = f"{primer_nombre} {apellido}"
    return nombre_completo.title()

trabajador = nombre_formateado("junior", "calderon")
print(trabajador)

