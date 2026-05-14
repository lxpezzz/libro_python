pedidos_bocadillos = ["calamares", "pepito de ternera", "jamón", "serranito"]

bocadillos_terminados = []
while pedidos_bocadillos:
    preparando_bocadillo = pedidos_bocadillos.pop()

    print(f"Su bocadillo de {preparando_bocadillo.title()} está listo.")
    bocadillos_terminados.append(preparando_bocadillo)

for bocadillo_terminado in bocadillos_terminados:
    print(f"\t{bocadillo_terminado.title()}")
