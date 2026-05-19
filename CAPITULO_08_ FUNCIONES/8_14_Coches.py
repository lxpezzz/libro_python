def crear_coche(fabricante, modelo, **desc_coche):
    desc_coche["fabricante"] = fabricante
    desc_coche["modelo"] = modelo

    return desc_coche


info_coche = crear_coche("BMW", "Serie 1", color="gris oscuro", puertas=5)
print(info_coche)
