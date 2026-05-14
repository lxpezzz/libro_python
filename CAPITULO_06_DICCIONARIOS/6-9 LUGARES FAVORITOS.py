lugares_favoritos = {
    "hector": ["roma", "amsterdam", "parís"],
    "nerea": ["castellón", "bolonia", "brasil"],
    "alfredo": ["valencia", "barcelona", "islas canarias"],
}
for nombre, lugares in lugares_favoritos.items():
    print(f"\nPara {nombre.title()} los sitios favoritos son:")
    for lugar in lugares:
        print(f"{lugar.title()}")
