### Se puede anidar diccionarios dentro de una lista.
# UNA LISTA DE DICCIONARIOS.
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Utilizamos el range() para generar la cantidad que queramos de elementos.
##
# Hace una lista vacía para guardar aliens
aliens = []

# Hacer 30 aliens verdes
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Muestra los 5 primeros aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Muesta cuántos aliens se han creado.
print(f"Total number of aliens: {len(aliens)}")

print("------------------------------------")

aliens = []

# Hacer 30 aliens verdes
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Muestra los 5 primeros aliens.
for alien in aliens[2:10]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:15]:
    print(alien)
print("....")

for alien in aliens[5:9]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 25

for alien in aliens[:15]:
    print(alien)
print("...")

## LISTA EN UN DICCIONARIO
# Guarda la info sobre una pizza que se está pidiendo.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}
# Resume el pedido.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t" + topping)

### Para poner una lista en un diccionario se puede usar:
favorite_languages = {
    "jen": ["python", "javascript"],
    "sarah": ["c", "c++"],
    "edward": ["rust", "java"],
    "phil": ["python", "rust"],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
