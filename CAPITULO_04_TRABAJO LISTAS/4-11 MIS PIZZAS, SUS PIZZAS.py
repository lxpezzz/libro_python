
pizzas = ['carbonara', '4 quesos', 'jamón y queso']

friend_pizzas = pizzas[:]

pizzas.append('pepperoni')
print(pizzas)

friend_pizzas.append('napolitana')
print(friend_pizzas)

print("\nMis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza.title())

print("\nLas pizzas de mi mejor amigo son:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())