animales = ['gato', 'perro', 'lince', 'tigre', 'loro']

print("\nEstos son los tres primeros elementos de la lista:")
for animal in animales [:3]:
    print(animal.title())

print("\nEstos 3 elementos están en el medio de la lista:")
for animal in animales [1:4]:
    print(animal.title())

print("\nEstos son los 3 últimos elementos de la lista:")
for animal in animales [-3:]:
    print(animal.title())