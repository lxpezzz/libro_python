## Se utiliza el bucel while para contar una serie de números.
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Dejar que el ususario elija cuándo salir.
# parrot.py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != "quit":
    message = input(prompt)
    print(message)

# Con una simplre prueba if, se puede eliminar el mensaje que sale al final del
# 'quit'
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)

# USAR UNA BANDERA
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)

# Usar break para salir de un bucle
# Para salir de un bucle while inmediatamente sin ejecutar nigún código dentro
# del bucle, podremos usar la sentencia BREAK.
prompt = "\nPLease enter the name of a city you hace visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")

## Usar continue en un bucle
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
print(current_number)
