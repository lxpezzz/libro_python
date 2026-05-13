pedidos_bocadillos = [
    "calamares",
    "pastrami",
    "pepito de ternera",
    "pastrami",
    "jamón",
    "serranito",
    "pastrami",
]
while "pastrami" in pedidos_bocadillos:
    pedidos_bocadillos.remove("pastrami")
print("No nos queda bocadillos de Pastrami, elige otro tipo de bocadillo.\n")

bocadillos_terminados = []
while pedidos_bocadillos:
    preparando_bocadillo = pedidos_bocadillos.pop()

    print(f"Su bocadillo de {preparando_bocadillo.title()} está listo.")
    bocadillos_terminados.append(preparando_bocadillo)

for bocadillo_terminado in bocadillos_terminados:
    print(f"\t{bocadillo_terminado.title()}")
