###
# La funciín input() pausa el programa
# y espera a que el usuario introduzca texto.
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

###
# Escribir indicaciones claras: Siempre que se use la fincion input(),
# deberemos incluir unas indicaciones claras y fáciles de seguir al usuario.
# Deberemos dejar un espacio despues de los :, para que el usuario responda al
# mensaje.

name = input("Please enter your name: ")
print(f"\nHello, {name}")

# A veces, necesitaremos escribir unas instrucciones de más de una línea.
prompt = "If you share your name, we can personaliza the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# Usar int() para aceptar entrada numérica.
