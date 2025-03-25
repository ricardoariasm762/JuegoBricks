def iniciar_juego():
    """Retorna un mensaje indicando que el juego ha iniciado."""
    return "¡Iniciando juego!!!"

def mover_personaje(direccion):
    """Retorna un mensaje indicando la dirección en la que se mueve el personaje."""
    if direccion not in ["arriba", "abajo", "izquierda", "derecha"]:
        raise ValueError("Dirección no válida")
    return f"Moviendo personaje hacia {direccion}"

def finalizar_juego():
    """Retorna un mensaje indicando que el juego ha finalizado."""
    return "¡Fin del juego!!"
