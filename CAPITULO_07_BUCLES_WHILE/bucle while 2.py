###
# Usar un bucle while con listas y diccionarios.
# Pasar elementos de una lista a otra.

# confirmed_users.py

# empuaza con usaurios que hay que verificar
# y una lista vacía para alojar a los usuarios confirmados.
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

# Verifica cada usuario hata que ya no hay ususarios sin confirmar.
# Mueve a cada usuario verificado a la lista de usuarios confirmados.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Muestra todos los usuarios confirmados.
print("\nThe following users have benn confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Eliminar todos los casos de valores específicos de una lista
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)

# Rellena un diccionario con entrada del usuario.
responses = {}

# Configura una bandera para indicar que la encuesta está activa.
polling_active = True

while polling_active:
    # Pide el nombre y la respuesta de la persona.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Guarda la respuesta en el diccionario
    responses[name] = response

    # Averigua si alguien más va a hacer la encuesta.
    repeat = input("Whould you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

# La encuesta está completa. Muestra los resultados.
print("\n--- Poll results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")
