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

    print(f"\tPaís: {info_ciudad['pais'].title()}")
    print(f"\tPoblacion: {info_ciudad['poblacion'].title()}")
    print(f"\tCuriosidad: {info_ciudad['curiosidad']}")
