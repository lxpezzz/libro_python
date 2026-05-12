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

    print(f"Verifyin user: {current_user.title()}")
    confirmed_users.append(current_user)

# Muestra todos los usuarios confirmados.
print("\nThe following users have benn confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_users.title())
