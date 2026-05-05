###
##Diccionarios sencillos.
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

##Trabajar con diccionarios:
# Es una colección de pares clave-valor.
# El diccionario va entre {}
# EJEMPLO:
alien_0 = {"color": "green", "points": 5}

# COMO ACCEDER A LOS VALORES DE UN DICCIONARIO:
alien_1 = {"color": "green"}
print(alien_0["color"])

alien_0 = {"color": "green", "points": 5}

new_points = alien_0["points"]
print(f"\nYou just earned {new_points} points!")

##AÑADIR NUEVOS PARES CLAVE-VALOR
# Se añade el nombre del diccionario seguido por la nueva clave entre corchetes
# junto con el nuevo valor.
alien_0 = {"color": "green", "points": 5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

##EMPEZAR CON UN DICCIONARIO VACÍO
alien_2 = {}

alien_2["color"] = "rojo"
alien_2["points"] = 10
print(alien_2)

##MODIFICAR VALORES EN UN DICCIONARIO
alien_0 = {"color": "green"}
print(f"The alien in {alien_0['color']}.")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}.")


alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"\nOriginal position: {alien_0['x_position']}")

# Mueve el alien hacia la derecha
# Determina cuánto se mueve el alien basándose en su velocidad actual.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # Debe se un alien rápido.
    x_increment = 3

# La nueva posición es la antigua más el incremento.
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']}")

print(alien_0)
alien_0["speed"] = "fast"
print(alien_0)

# ELIMINAR PARES CLAVE-VALOR
# Se utiliza el DEL para eliminar por completo un par clave-valor.
alien_0 = {"color": "green", "points": 25}
print(alien_0)

del alien_0["points"]
print(alien_0)
# Hay que tener en cuenta que el par clave-valor eliminado se borrará de manera
# permanente.

# Diccionaris de objetos similares.
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}")

##
# Usar get() para acceder a valores.
# Si la clave que pedimos NO existe, nos dara un error 'KEYERROR':'CLAVW QUE FALTA'
# El método get() se usa para configurar un valor predetermindao que se devuelva
# si la clave solicitada no existe.

alien_0 = {"color": "green", "speed": "slow"}

point_value = alien_0.get("points", "No point value assigned.")
print(point_value)

# Si cabe la posibilidad de que no exista la clave que busca,
# considere usar el método get() en vez de la notación de los corchetes.
