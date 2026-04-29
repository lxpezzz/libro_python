lista_invitados = ['Messi', 'Jordan', 'Cristiano', 'Papa']
#Invitaciones iniciales
mensaje_cena1 = f"Hola, me encantaría que vinieses a mi cena, eres mi ídolo, {lista_invitados[0]}"
mensaje_cena2 = f"Te invito a mi cena porque te quiero conocer en persona, {lista_invitados[1]}"
mensaje_cena3 = f"Si vienes a la cena, haré un SIUUU, {lista_invitados[2]}"
mensaje_cena4 = f"A mi abuela le encantaría conocerte, {lista_invitados[3]}"

print(mensaje_cena1)
print(mensaje_cena2)
print(mensaje_cena3)
print(mensaje_cena4)
#No puede asistir
no_asiste = lista_invitados.pop(2)
print(f"El invitado {no_asiste}, no podrá venir a la fiesta por motivos personales.")

#Sustituto
lista_invitados.insert(3, 'Lamine Yamal')

#Nueva lista de invitados
for invitados in lista_invitados: 
    print(f"Hola, {invitados} te envío la nueva invitación a la reunión.")

print(lista_invitados)