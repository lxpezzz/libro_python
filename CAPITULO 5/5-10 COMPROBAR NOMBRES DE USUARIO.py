current_users = ["alfredo", "hector", "ana", "nerea", "irene"]
new_users = ["alfredo", "nerea", "maria", "cesar", "lamine"]

for new_user in new_users:
    if new_user in current_users:
        print(f"\n{new_user.title()}, introduce otro nombre. Ese ya está en uso.")
    else:
        print(f"\n{new_user.title()}, el nombre de usuario esta disponible.")


##
current_users = ["Alfredo", "Hector", "Ana", "Nerea", "Irene"]
new_users = ["alfredo", "nerea", "maria", "cesar", "lamine"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"\n{new_user.title()}, introduce otro nombre. Ese ya está en uso.")
    else:
        print(f"\n{new_user.title()}, el nombre de usuario está disponible.")
