# tests/test_game_utils.py
import pytest
from src.funJuego import iniciar_juego, mover_personaje, finalizar_juego

# ==============================
# Prueba 1: iniciar_juego()
# ==============================
def test_iniciar_juego():
    """Verifica que iniciar_juego retorna el mensaje esperado."""
    assert iniciar_juego() == "¡Iniciando juego!!!"

# ==============================
# Prueba 2: mover_personaje()
# ==============================
@pytest.mark.parametrize(
    "direccion, expected",
    [
        ("arriba", "Moviendo personaje hacia arriba"),
        ("abajo", "Moviendo personaje hacia abajo"),
        ("izquierda", "Moviendo personaje hacia izquierda"),
        ("derecha", "Moviendo personaje hacia derecha"),
    ],
)
def test_mover_personaje(direccion, expected):
    """Verifica que mover_personaje retorna el mensaje correcto según la dirección."""
    assert mover_personaje(direccion) == expected

def test_mover_personaje_direccion_invalida():
    """Verifica que mover_personaje lanza un error cuando la dirección no es válida."""
    with pytest.raises(ValueError):
        mover_personaje("diagonal")

# ==============================
# Prueba 3: finalizar_juego()
# ==============================
def test_finalizar_juego():
    """Verifica que finalizar_juego retorna el mensaje esperado."""
    assert finalizar_juego() == "¡Fin del juego!!"
