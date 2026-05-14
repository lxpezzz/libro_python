platos = ('tortilla', 'paella', 'croquetas', 'patatas bravas', 'sepia')
print(platos)

for plato in platos: 
    print(plato.title())


print("\nEsta es la carta que tenemos en el menú:")
for plato in platos: 
    print(plato.title())

platos = ('tortilla', 'paella', 'croquetas', 'jamón', 'chuletas')

print("\nEsta es la nueva carta que tenemos en el restaurante:")
for plato in platos:
    print(plato.title())



platos = ('tortilla', 'paella', 'croquetas', 'patatas bravas', 'sepia')
platos[0] = 'arroz'