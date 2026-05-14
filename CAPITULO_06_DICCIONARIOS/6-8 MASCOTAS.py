mascotas_0 = {"tipo": "perro", "dueño": "hector"}
mascotas_1 = {"tipo": "gato", "dueño": "ana"}
mascotas_2 = {"tipo": "caballo", "dueño": "nerea"}
mascotas_3 = {"tipo": "cacatúa", "dueño": "alfredo"}
mascotas = [mascotas_0, mascotas_1, mascotas_2, mascotas_3]
for mascota in mascotas:
    print(f"\nMascota = {mascota['tipo'].title()}, {mascota['dueño'].title()}")
