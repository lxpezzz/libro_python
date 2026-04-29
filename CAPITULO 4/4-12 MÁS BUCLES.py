my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('apple')
friend_foods.append('rice')

print("\nMy favourite foods are:")
for my_food in my_foods:
    print(my_food.title())

print("\nMy friend`s favourite foods are:")
for friend_food in friend_foods:
    print(friend_food.title())