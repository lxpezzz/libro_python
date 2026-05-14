def ciudad_pais(ciudad, pais):
    ubicacion = f"{ciudad}, {pais}"
    return ubicacion.title()


print(ciudad_pais("santiago", "chile"))
print(ciudad_pais("madrid", "españa"))
print(ciudad_pais("paris", "francia"))
