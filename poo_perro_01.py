

class Dog:
    """"Un intento sencillo de modelar un perro"""
    
    def __init__(self, name, age):
        """inicializa los atributos name y age"""
        self.name = name
        self.age = age
        
        
    def sit(self):
        """simula un perro sentandoce al darle la orden"""
        print(f"{self.name} esta ahora sentado")
        
    def roll_over(self):
        """simula un perro dandoce la vuelta al darle la orden"""
        print(f"{self.name} ahora se da vueltas")
        
my_dog = Dog("puzo", 6)
your_dog = Dog("bandido", 3)


print(f"Mi perro se llama {my_dog.name}.")
print(f"Mi Perro {my_dog.name} tiene {my_dog.age} años de edad.")
my_dog.sit()
my_dog.roll_over()
print("\n")
print(f"Mi perro se llama {your_dog.name}.")
print(f"Mi Perro {your_dog.name} tiene {your_dog.age} años de edad.")
your_dog.sit()
your_dog.roll_over()