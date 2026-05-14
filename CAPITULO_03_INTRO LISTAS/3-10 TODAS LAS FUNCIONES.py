rios = ['Ebro', 'Mijares', 'Tajo', 'Nilo']
print(rios)

rios.append('Támesis')
print(rios)

rios.insert(0, 'Elba')
print(rios)

del rios[0]
print(rios)

popped_rios = rios.pop()
print(rios)
print(popped_rios)

rios.remove('Tajo')
print(rios)

rios = ['Ebro', 'Mijares', 'Tajo', 'Nilo']
print(rios)
rios.sort()
print(rios)

rios.sort(reverse=True)
print(rios)

rios = ['Ebro', 'Mijares', 'Tajo', 'Nilo']
print(sorted(rios))


rios = ['Ebro', 'Mijares', 'Tajo', 'Nilo']
rios.reverse()
print(rios)

rios = ['Ebro', 'Mijares', 'Tajo', 'Nilo']
print(len(rios))
print(f"Hay {len(rios)} ríos, en la lista.")