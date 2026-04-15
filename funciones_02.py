"""PASAT INFORMACION A LA FUNCION 
si modifica ligeramente la funcion saludar_al_usuario() puede saludar al usuario por su nombre. para que funcione haga esto ingresa username entre parentesis de la definicion de la funcion en def saludar_al_usuario() al agregar username aqui, permite que la funcion acepte cualquier valor de username cada vez que la llames. cuando llamas a saludar_al_usuario(), puedes pasarle un nombre, como 'jose' dentro del parentesis:"""
def saludar_al_usuario(username) :
    """muestra un simple saludo."""
    print(f"hola, {username.title()}!")
saludar_al_usuario("jose")