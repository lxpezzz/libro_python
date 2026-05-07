rios_importantes = {"nilo": "egipto", "ebro": "españa", "tamesis": "inglaterra"}
# Junta el río con el país.
for rio, pais in rios_importantes.items():
    print(f"El {rio.title()} discurre por {pais.title()}.")

rios_importantes = {"nilo": "egipto", "ebro": "españa", "tamesis": "inglaterra"}
# Solo rios
print("\nRíos:")
for rio in rios_importantes.keys():
    print(rio.title())

# Solo paises.
print("\nPaíses:")
for pais in rios_importantes.values():
    print(pais.title())
