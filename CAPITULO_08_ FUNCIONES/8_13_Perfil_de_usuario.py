def build_profile(nombre, apellido, segundo_apellido, **user_info):
    """Crea un diccionario con todo lo que sabemos sobre un usuario."""
    user_info["nombre"] = nombre
    user_info["apellido"] = apellido
    user_info["ult_apellido"] = segundo_apellido
    return user_info


user_profile = build_profile(
    "héctor",
    "lópez",
    "díaz",
    localidad="castellón",
    profesion="analista de datos",
    equipo="barcelona",
)
print(user_profile)
