"""PRUEBELO USTED MISMO POO  9-1 
Restaurante: crea una clase llamada Restaurant. El método __init__() para
Restaurant debe almacenar dos atributos: un restaurant _ name y un cuisine _ type.
Cree un método llamado describe_restaurant() que imprima estos dos datos y un método
llamado open_restaurant() que imprima un mensaje indicando que el restaurante estå
abierto.
Crea una instancia llamada restaurant de tu clase. Imprima los dos atributos
individualmente y luego llame a ambos métodos."""

class Restaurant:
    """descricion de la clase"""
    def __init__(self, name, tipe):
        """inizializa los atributos mame y tipe"""
        self.name = name
        self.tipe = tipe
        
    def describe_restaurant(self):
        """describe el tipo de restaurant"""
        print(f"El restaurant {self.name} es de comida {self.tipe}")
    
    def open_restaurant(self):
        """indica la hora de apetura del restaurant"""
        print(f"el restaurant {self.name} esta abierto")


restauran = Restaurant("el pomodoro", "Italiana")
print(restauran.name)
print(restauran.tipe)

restauran.describe_restaurant()
restauran.open_restaurant()