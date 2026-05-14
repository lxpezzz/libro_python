reserva = input("¿Cuántos vendréis a cenar? ")
reserva = int(reserva)

if reserva > 8:
    print("\tTendréis que esperar a que se vaya una mesa.")
else:
    print("\tSu mesa está lista.")


### VERSION MEJORADA CON EXCEPCIÓN POR SI ESCRIBEN OTRA COSA QUE NO SEA NÚMERO.
try:
    reserva = int(input("¿Cuántos vendréis a cenar? "))

    if reserva > 8:
        print("\tTendréis que esperar a que se libere una mesa.")
    else:
        print("\tSu mesa está lista.")

except ValueError:
    print("\tIntroduce un número válido.")
