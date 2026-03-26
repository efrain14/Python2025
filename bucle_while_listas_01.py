""" MOVER ELEMENTOS DE UNA LISTA A OTRA
Considere una lista de usuarios recién registrados pero no
verificados de un sitio web. Después de verificar a estos usuarios,
¿cómo podemos moverlos a una lista separada de usuarios
confirmados? Una forma sería utilizar un bucle while para extraer
usuarios de la lista de usuarios no confirmados a medida que los
verificamos y luego agregarlos a una lista separada de usuarios
confirmados. Así es como podría verse ese código:"""

# comiensa con la lista de los usuarios que nesesitan ser verificados
# has una lista vacia con los usuarios que ya fueron verificados

usuarios_por_confirmar = ["pedro", "luis", "maria", "junior"]

usuarios_confirmados = []

# verificar cada usuario hasta que no queden usuarios no confirmados
# mover cada usuario verificado a la lista de usuarios confirmados

while usuarios_por_confirmar :
    usuario_actual = usuarios_por_confirmar.pop()
    
    print(f"usuario verificado : {usuario_actual.title()}")
    usuarios_confirmados.append(usuario_actual)
    
# muestra todos los usuarios confirmados
print("\nLos siguientes usuarios han sido confirmados:")
for usuarios_confirmado in usuarios_confirmados :
    print(usuarios_confirmado.title())