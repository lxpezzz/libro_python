def hacer_album(artista, titulo, num_canciones=None):
    dic_album = {
        "artista": artista,
        "titulo": titulo,
    }
    if num_canciones:
        dic_album["num_canciones"] = num_canciones
    return dic_album


while True:
    print("\nDime tu artista y título favorito:")
    print("(Usa 'q' para salir del comando.)")

    info_artista = input("Artista: ")
    if info_artista == "q":
        break

    info_titulo = input("Título: ")
    if info_titulo == "q":
        break

    album_perso = hacer_album(info_artista, info_titulo)
    print("\n Álbum creado:")
    print(album_perso)
