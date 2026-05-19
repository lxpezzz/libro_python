def make_sandwich(*ingredientes):
    """Imprime la lista de ingredientes solicitados."""
    print("\nPreparando el sandwich con los ingredientes solicitados:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente.title()}")


make_sandwich("jamón serrano")
make_sandwich("queso", "jamón york")
make_sandwich("aguacate", "pollo", "lechuga")
