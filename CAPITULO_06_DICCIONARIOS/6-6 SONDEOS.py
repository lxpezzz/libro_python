favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

encuesta = ["jen", "nerea", "alfredo", "phil"]

for persona in encuesta:
    if persona in favorite_languages.keys():
        print(f"\n{persona.title()}, ¡Gracias por responder!")
    else:
        print(f"\n{persona.title()}, recuerda hacer la encuesta.")
