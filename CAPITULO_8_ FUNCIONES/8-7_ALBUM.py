def hacer_album(artista, titulo, num_canciones=None):
    dic_album = {
        "artista": artista,
        "titulo": titulo,
    }
    if num_canciones:
        dic_album["num_canciones"] = num_canciones

    return dic_album


album_1 = hacer_album("bad bunny", "debí tirar más fotos", 17)
album_2 = hacer_album("cano", "anais", 10)
album_3 = hacer_album(
    "dellafuente",
    "torii yama",
)
print(album_1)
print(album_2)
print(album_3)
