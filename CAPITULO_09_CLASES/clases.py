## Crear y usar una clase
# Creación de la clase Dog
class Dog:
    """Un intento sencillo de modelar un perro."""

    def __init__(self, name, age):
        """INicializa los atributos de nombre y edad."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula un perro sentándose en respesta a una orden."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simula hacer la croqueta en respuesta a una orden."""
        print(f"{self.name} rolled over")


# Los nombres de las clases en Python se escriben en mayúsculas.
# El método __init__()
# Hacer una instacia de una clase
my_dog = Dog("Willie", 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age} years old")
