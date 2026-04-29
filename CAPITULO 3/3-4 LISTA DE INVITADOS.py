lista_invitados = ['Messi', 'Jordan', 'Cristiano', 'Papa']

mensaje_cena1 = f"Hola, me encantaría que vinieses a mi cena, eres mi ídolo, {lista_invitados[0]}"
mensaje_cena2 = f"Te invito a mi cena porque te quiero conocer en persona, {lista_invitados[1]}"
mensaje_cena3 = f"Si vienes a la cena, haré un SIUUU, {lista_invitados[2]}"
mensaje_cena4 = f"A mi abuela le encantaría conocerte, {lista_invitados[3]}"

print(mensaje_cena1)
print(mensaje_cena2)
print(mensaje_cena3)
print(mensaje_cena4)


###
#Modo fácil de hacerlo con el bucle for, para enviar el mismo mensaje a varios elementos de la lista.
#
for invitado in lista_invitados:
    print(f"Hola {invitado}, estás invitado a mi cena")