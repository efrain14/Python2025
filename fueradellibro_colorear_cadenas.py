import colorama
from colorama import init, Fore, Back, Style
colorama.init()

print(Fore.YELLOW + "Hola Mundo")
print(Fore.RED + "Hola Mundo")
print(Fore.BLUE + "Hola Mundo")
print(Fore.CYAN + "Hola Mundo")
print(Fore.GREEN + "Hola Mundo")
colorama.deinit()# resetea los colores de la terminal al finalizar