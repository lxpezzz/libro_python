lista_invitados = ['Messi', 'Jordan', 'Cristiano', 'Papa']
#Invitaciones iniciales
mensajes = [
    f"Hola, me encantaría que vinieses a mi cena," 
    f"eres mi ídolo, {lista_invitados[0]}"
    f"Te invito a mi cena porque te quiero conocer" 
    f"en persona, {lista_invitados[1]}"
    f"Si vienes a la cena, haré un SIUUU, {lista_invitados[2]}"
    f"A mi abuela le encantaría conocerte, {lista_invitados[3]}"]

for mensaje in mensajes:
    print(mensaje)
#No puede asistir
no_asiste = lista_invitados.pop(2)
print(f"El invitado {no_asiste}, " 
      f"no podrá venir a la fiesta por motivos personales.")

#Sustituto
lista_invitados.insert(3, 'Lamine Yamal')

#Nueva lista de invitados
for invitados in lista_invitados: 
    print(f"Hola, {invitados} te envío la nueva invitación a la reunión.")

print(lista_invitados)