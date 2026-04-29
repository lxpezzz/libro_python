#Se añaden 3 elementos a la lista

lista_invitados = ['Messi', 'Jordan', 'Papa', 'Lamine Yamal']

for invitados in lista_invitados: 
    print(f"{invitados}, se han conseguido más invitaciones.")


##Para añadir elementos a las listas se utiliza insert, pero si quiero añadir al final de la lista el elemento
#utilizo append

lista_invitados.insert(0, 'Vinicius')
lista_invitados.insert(2, 'Confucio')
lista_invitados.append('Jeff Bezos')

for invitados in lista_invitados:
    print(f"{invitados}, esta es la nueva invitación, se ruega confirmación antes de que sea el evento")

print(lista_invitados)