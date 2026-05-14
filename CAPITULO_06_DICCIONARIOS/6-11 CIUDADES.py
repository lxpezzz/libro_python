ciudades = {
    "madrid": {
        "pais": "España",
        "poblacion": "3.500.000",
        "curiosidad": "Madrid alberga el restaurante más antiguo"
        "del mundo aún en funcionamiento, el Sobrino de Botín, "
        "fundado en 1725 y famoso por su cochinillo asado",
    },
    "parís": {
        "pais": "Francia",
        "poblacion": "2.100.000",
        "curiosidad": "la Torre Eiffel crece hasta "
        "18 cm en verano por la dilatación del hierro",
    },
    "roma": {
        "pais": "Italia",
        "poblacion": "2.700.000",
        "curiosidad": "Roma es un museo al aire libre "
        "con más de 2700 años de historia, famosa por albergar al Vaticano",
    },
}

for ciudad, info_ciudad in ciudades.items():
    print(f"\nCiudad: {ciudad.title()}")
    info_ciudad_pais = f"{info_ciudad['pais']}"
    info_ciudad_poblacion = f"{info_ciudad['poblacion']}"
    info_ciudad_curiosidad = f"{info_ciudad['curiosidad']}"

    print(f"\tPaís: {info_ciudad_pais.title()}")
    print(f"\tPoblacion: {info_ciudad_poblacion}")
    print(f"\tCuriosidad: {info_ciudad_curiosidad}")
