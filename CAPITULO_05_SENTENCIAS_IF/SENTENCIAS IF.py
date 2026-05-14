###

##Para hacer una comprbación de igualdad  se hace así:

requested_topping = "anchovies"
if requested_topping == "anchovies":
    print("\nHold the anchovies!\n")

##Para hacer una comprbación de desigualdad  se hace así:
requested_topping2 = "mushrooms"
if requested_topping2 != "anchovies":
    print("Hold the mushrooms!")

##Comprobaciones numéricas:

answer = 17

if answer == 17:
    print("\nYou are right!")

if answer != 18:
    print("\nYou are wrong!")

# Usar "and" para comprobar varias condiciones:
age_0 = 22
age_1 = 18
if age_0 <= 21 and age_1 >= 21:
    print("\nTrue")
else:
    print("\nFalse")

age_1 = 22
if age_0 >= 21 and age_1 >= 21:
    print("\nTrue")
else:
    print("\nFalse")

# Usar "or" para comprobar varias condiciones.
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print("\nVerdadero")
else:
    print("\nFalso")

age_0 = 18
if age_0 >= 21 or age_1 >= 21:
    print("\nFalse")
else:
    print("\nPatata")

# Comprobar si hay un elemento en una lista:
requested_toppings = ["mushrooms", "onions", "pineapple"]
if "mushrooms" in requested_toppings:
    print("\nSetas")

# Comprobar si no hay un elemento en una lista:

banned_users = ["andrew", "micaela", "carolina"]
user = "marie"
if user not in banned_users:
    print(f"\n{user.title()}, you can post a response if you wish.")

# Expresiones booleanas.
# Ejemplo de expresion booleanas:

marcas = "nike"
print("\n¿'nike' está en marcas? Predicción: True")
print("nike" in marcas)

game_active = True
can_edit = False
