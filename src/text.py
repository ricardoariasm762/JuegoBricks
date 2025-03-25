def read_file(filename):
    """Lee el contenido de un archivo de texto."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def write_file(filename, content):
    """Escribe contenido en un archivo de texto."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def append_to_file(filename, content):
    """Agrega contenido al final de un archivo de texto."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content + "\n")
