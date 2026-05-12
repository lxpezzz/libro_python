### 1) PRUEBA CONDICIONA EN LA SENTENCIA WHILE PARA DETENER EL BUCLE.
pizza = "\nIntroduzca los ingredientes de la pizza: "
pizza += "\nCuando acabes escribe 'quit'."

message = ""
while message != "quit":
    message = input(pizza)

    if message != "quit":
        print(message)

### 2) VARIABLE ACTIVE PARA CONTROLAR CUÁNTO TIEMPO SE EJECUTA EL BUCLE.

pizza = "\nIntroduzca los ingredientes de la pizza: "
pizza += "\nCuando acabes escribe 'quit'."

active = True
while active:
    ingrediente = input(pizza)

    if ingrediente == "quit":
        active = False
    else:
        print(f"\tAñadido: {ingrediente.title()}")

### Sentencia break para salir del bucle cuando el usuariointroduzca el valor
# 'quit.
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
