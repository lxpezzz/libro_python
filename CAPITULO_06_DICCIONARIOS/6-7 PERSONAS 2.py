info_nombre_0 = {
    "nombre": "héctor",
    "apellido": "lópez",
    "edad": 24,
    "ciudad": "castellón",
}
info_nombre_1 = {
    "nombre": "nerea",
    "apellido": "alegre",
    "edad": 21,
    "ciudad": "castellón",
}
info_nombre_2 = {
    "nombre": "alfredo",
    "apellido": "lópez",
    "edad": 24,
    "ciudad": "valencia",
}
personas = [info_nombre_0, info_nombre_1, info_nombre_2]
for persona in personas:
    print(f"Nombre: {persona['nombre'].title()}")
    print(f"Apellido: {persona['apellido'].title()}")
    print(f"Edad: {persona['edad']}")
    print(f"Ciudad: {persona['ciudad'].title()}")
    print()
