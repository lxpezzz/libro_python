## Pasar un número arbitriario de argumentos.
# Con el parámetro *lista, recoge todos los argumentos que le proporcione
# la línea de la llamada.
def make_pizza(*toppings):
    """Imprime la lista de ingredientes solicitados."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# El * en el nombre del parámetro *toppings le indica a Python
# que cree una tupla vacía llamada toppings, que conenga todos los valores
# que reciba esta función.


def make_pizza(*toppings):
    """Imprime la lista de ingredientes solicitados."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# Mezclar argumentos posicionales y arbitrarios.
print("Pequeña - 1, mediana - 2, grande - 3")
def make_pizza(size, *toppings):
    """Imprime la lista de ingredientes solicitados."""
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza(2, "pepperoni")
make_pizza(1, "mushrooms", "green peppers", "extra cheese")

# Usar argumentos de palabra clave arbitrarios.
def build_profile(first, last, **user_info):
    """Crea un diccionario con todo lo que sabemos sobre un usuario."""
    user_info['first_name'] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
        location='princenton',
        field='physics')
print(user_profile)