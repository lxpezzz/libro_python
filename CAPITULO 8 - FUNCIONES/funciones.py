## Definir una función
def greet_user():
    print("Hello!")


greet_user()


## Pasar información a una función
def greet_user(username):
    print(f"Hello, {username.title()}")


greet_user("jesse")

##Argumentos y parámetros
"""Un argumento es una información que se pasa desde una función para llamar
a una función"""


## Pasar argumentos
# Argumentos posicionales.
def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hamster", "harry")


# Múltiples llamadas a una función
def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hamster", "harry")
describe_pet("dog", "nuska")


## Argumentos de palabra clave
def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


print("\n------------------------")
describe_pet(animal_type="hamster", pet_name="harry")
