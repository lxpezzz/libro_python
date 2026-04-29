lista_invitados = ['Vinicius', 'Messi', 'Confucio', 'Jordan', 'Papa', 'Lamine Yamal', 'Jeff Bezos']

print("Disculpad, pero al final solo puedo invitar a 2 personas.")

eliminado = lista_invitados.pop()
print(f"Lo siento pero al final no puedo invitarte, {eliminado}")
eliminado = lista_invitados.pop()
print(f"Lo siento pero al final no puedo invitarte, {eliminado}")
eliminado = lista_invitados.pop()
print(f"Lo siento pero al final no puedo invitarte, {eliminado}")
eliminado = lista_invitados.pop()
print(f"Lo siento pero al final no puedo invitarte, {eliminado}")
eliminado = lista_invitados.pop()
print(f"Lo siento pero al final no puedo invitarte, {eliminado}")

for invitados in lista_invitados:
    print(f"{invitados.title()}, sigues invitado a la cena que voy a celebrar mañana. Por favor, confirmar asistencia.")

del lista_invitados[0]
del lista_invitados[0]

print(lista_invitados)

