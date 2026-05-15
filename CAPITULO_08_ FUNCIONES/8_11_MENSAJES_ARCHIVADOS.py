msg_cortos = ["te amo", "hola buenas", "¿Qué tal?", "¿Cómo estás?"]
msg_enviados = []


def mostrar_mensaje(mensajes):
    for mensaje in mensajes:
        print(mensaje.title())


def enviar_mensajes(msg_cortos, msg_enviados):
    while msg_cortos:
        mensaje = msg_cortos.pop()
        print(f"Mensaje enviado: {mensaje.title()}")
        msg_enviados.append(mensaje)


mostrar_mensaje(msg_cortos)
enviar_mensajes(msg_cortos[:], msg_enviados)
print(msg_cortos)
print(msg_enviados)
