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
# Transforma la entrada en un valor numérico

# Hay que convertir primer el valor de la entrada en una representación
# numérica.
# Ejemplo:
height = input("How tall are you, in cm? ")
height = int(height)

if height >= 130:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# El operador módulo (%)
# Se utiliza para trabajar con valores numéricos.
# Lo que hace es dividir un número entre otro y devolver el resto

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
