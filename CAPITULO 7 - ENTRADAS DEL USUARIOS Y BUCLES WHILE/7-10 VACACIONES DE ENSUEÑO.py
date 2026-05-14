vacaciones_sueños = {}

active = True

while active:
    nombre = input("\n¿Cuál es tu nombre?")
    lugar = input("\nSi pudieras visitar cualquier lugar del mundo," "¿Dónde irías?")
    repeat = input("\nTe gustaría que alguien mas responda a la pregunta?")
    vacaciones_sueños[nombre] = lugar
    if repeat == "no":
        active = False

print("\n---Resultados de la encuesta---")
for nombre, lugar in vacaciones_sueños.items():
    print(f"\nA {nombre.title()} le encantaría ir a {lugar.title()}.")
