"""FUNCIONES  Hecar que un argumento sea opcional 
A veces tiene sentido hacer que un argumento sea opcional, de
modo que las personas que usan la función puedan optar por
proporcionar información adicional solo si así lo desean. Puede
utilizar valores predeterminados para hacer que un argumento sea
opcional.
Por ejemplo, digamos que queremos expandir nombre_formateado()
para manejar también los segundos nombres. Un primer intento de
incluir segundos nombres podría verse así:"""

def nombre_formateado(primer_nombre, segundo_nombre, apellido):
    """funcion que formatea un nombre"""
    nombre_completo = f"{primer_nombre} {segundo_nombre} {apellido}"
    return nombre_completo.title()

trabajador = nombre_formateado("willy", "faviolo", "garcia")
print(trabajador)