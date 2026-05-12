pizza = "\nIntroduza los ingredientes de la pizza: "
pizza += "\nCuando acabes escribe 'quit'."

while True:
    ingrediente = input(pizza)

    if ingrediente == "quit":
        break
    else:
        print(f"\tAñadido: {ingrediente.title()}")
