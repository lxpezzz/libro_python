entradas = "\nEscriba su edad: "
entradas += "\nCuando acabes escribe 'quit'."

while True:
    edad = input(entradas)
    if edad == "quit":
        break

    edad = int(edad)

    if edad < 3:
        print("\tLa entrada es gratuita.")
    elif edad <= 12:
        print("\tLa entrada cuesta 8€.")
    else:
        print("\tLa entrada cuesta 12€.")
