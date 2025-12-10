"""PRUEBELO USTED MISMO 6-6 
HAGA UNA LISTA DE PERSONAS QUE DEBERIAN REALIZAR LA ENCUESTA DE IDIOMA FAVORITO DE PROGRAMACION, RECORRA LA LISTA  DE PERSONAS QUE DEBERIAN REALIZAR LA ENCUESTA SI YA LA REALIZARON IMPRIMA UN MENSAJE AGRADECIENDOLES POR RESPONDER, SI AUN NO HAN REALIZADO LA ENCUESTA, IMPRIMA UN MENSAJE INVITANDOLES A REALIZARLA"""

lenguajes_favoritos = {
    "jose" : "python",
    "pedro" : "rust",
    "maria" : "java",
    "alexander" : "PHP",
    "violeta" : "C",
    "efrain" : "python"
    }
for nombre , lenguaje in lenguajes_favoritos.items():
    print(f"gracias {nombre} por haber realizado la encuesta de lenguajes de programacion")