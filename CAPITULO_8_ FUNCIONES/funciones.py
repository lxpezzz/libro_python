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


## Valores de retorno.
# Devolover un solo valor.
def get_formatted_name(first_name, last_name):
    """Devuelve un nombre completo, con un formato adecuado."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)


## Usar una función con un bucle WHILE.
def get_formatted_name(first_name, last_name):
    """Devuelve un nombre completo, con un formato adecuado."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# ¡Esto es un bucle infinito!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


## Pasar una lista.
def greet_users(names):
    """Imprime un saludo secillo para cada usuario de la lista."""
    for name in names:
        msg = f"Hello, {name.title()}"
