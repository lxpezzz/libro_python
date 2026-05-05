names = []

if names:
    for name in names:
        if name == "admin":
            print("\nHola admin, ¿quieres ver un informe de estado?")
        else:
            print(f"\nHola {name.title()}, gracias por volver a entrar.")
else:
    print("\nNecesitamos encontrar algunos usuarios.")
