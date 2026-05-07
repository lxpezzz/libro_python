num_fav = {
    "hector": [10, 7],
    "nerea": [7, 8],
    "alfredo": [6, 5],
    "ana": [5, 8],
    "irene": [3, 7],
}

for nombre, numeros in num_fav.items():
    print(f"\nLos números favoritos de {nombre.title()} son {numeros}")

## Está bien hecho pero se puede mejorar así:
num_fav = {
    "hector": [10, 7],
    "nerea": [7, 8],
    "alfredo": [6, 5],
    "ana": [5, 8],
    "irene": [3, 7],
}

for nombre, numeros in num_fav.items():
    print(f"\nLos números favoritos de {nombre.title()} son:")

    for numero in numeros:
        print(numero)
