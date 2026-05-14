words_python = {
    "lista": "Colección ordenada de elementos. Entre []",
    "booleano": "Se usa para representar condiciones lógicas. True or False",
    "diccionario": "Almacena datos mediante pares: clave : valor",
    "tabulacion": "Espacio al inicio de una línea que Python usa para definir bloques de código.",
    "sentencia if": "Permite ejecutar código solo si una condición es verdadera.",
    "funcion": "Bloque de código reutilizable que realiza una "
    "tarea específica. Se define con def.",
    "variable": "Espacio en memoria donde se almacena un dato "
    "para poder utilizarlo después.",
    "tupla": "Colección ordenada e inmutable de elementos. "
    "Se define con paréntesis ().",
    "f-string": "Forma moderna de insertar variables dentro de "
    "un texto usando f'' o f",
    "excepcion": "Error que ocurre durante la ejecución del "
    "programa y puede manejarse con try y except.",
}
for word, definicion in words_python.items():
    print(f"{word.title()}: {definicion}")
