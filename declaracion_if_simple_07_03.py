"""Comprobacion de Nombre de usuario"""
#Haga lo siguiente para crear un programa que simule cómo los sitios web
# garantizan que todos tengan un nombre de usuario único.

#Crea una lista de cinco o más nombres de usuario llamados current_users. Crea
# otra lista de cinco nombres de usuario llamados new_users. Asegúrate de que
# uno o dos de los nuevos nombres de usuario también estén en la
# current_userslista.

#Revise la new_userslista para ver si ya se ha usado cada nuevo nombre de
# usuario. De ser así, imprima un mensaje indicando que la persona deberá
# ingresar un nuevo nombre de usuario. Si no se ha usado ningún nombre de
# usuario, imprima un mensaje indicando que está disponible.

#Asegúrese de que su comparación no distinga entre mayúsculas y minúsculas.
# Si 'John'se ha usado, 'JOHN'no debe aceptarse. (Para ello, deberá crear una
# copia que current_userscontenga las versiones en minúsculas de todos los
# usuarios existentes)#
current_users = ["JOHN", "jose", "pedro", "luis", "CARLOS","rosa", "luisa"]
new_users = ["miguel", "antonio","JOHN", "efrain", "rosa"]
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"lo sentimos {new_user} este nombre ya esta siendo usado, devera de elegir otro nombre de usuario")
    else:
        print(f"estupendo, el nombre {new_user} esta disponible")
print("\n")
print(current_users)
print(current_users_lower)