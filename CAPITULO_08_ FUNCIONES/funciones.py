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
    ## He puesto esto en comentario porque sino no se puede ejcutar
    # más código.
    ### while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


## Pasar una lista.
def greet_users(names):
    """Imprime un saludo sencillo para cada usuario de la lista."""
    for name in names:
        msg = f"Hello"


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)


print("---------")
## Modificar una lista en una función.
# Cuando se haga un cambio en la lista dentro de la función es permanente.
#####EJemplo:
# Empieza con unos diseños que hay que imprimir.
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# Simula la impresión de cada diseño hasta que no queda ninguno.
# Mueve cada diseño a completed_models después de la impresión.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Muesta todos los modelos completados.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# Se puede reorganizar este código escribiendo 2 funciones:
def print_models(unprinted_designs, completed_models):
    """
    Simula imprimir cada diseño, hasta que no queda ninguno.
    Mueve cada diseño a completed_designs después de la impresión
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Muestra todos los modelos que se ha imprimido."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

## Evita que una función modifique una lista.
# Se envía una copia de una lista a una función:
# nombre_funcion(nombre_lista[:])
"""
La notación para partir[:] hace una copia de la lista y se la envía a la función
"""
