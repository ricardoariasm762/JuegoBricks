import pytest
import random
from src.carreras import Car, race

# ==============================
# Prueba 1: Creación de auto
# ==============================
def test_car_initial_position():
    """Verifica que un auto recién creado tiene posición 0."""
    car = Car("Test Car")
    assert car.position == 0

# ==============================
# Prueba 2: Avance del auto
# ==============================
def test_car_advance(monkeypatch):
    """Verifica que el auto avanza en el rango esperado (1 a 6)."""
    car = Car("Test Car")

    # Simulamos que el random siempre devuelve 3
    monkeypatch.setattr(random, "randint", lambda a, b: 3)

    car.advance()
    assert car.position == 3  # Avanzó exactamente 3 unidades

# ==============================
# Prueba 3: Carrera con autos
# ==============================
def test_race_winner(monkeypatch):
    """Simula una carrera y verifica que hay un ganador."""
    
    # Creamos tres autos
    cars = [Car("Auto 1"), Car("Auto 2"), Car("Auto 3")]

    # Simulamos que cada avance es 5 (forzamos el resultado del random)
    monkeypatch.setattr(random, "randint", lambda a, b: 5)

    winner = race(cars, finish_line=10)  # La meta es 10

    assert any(car.position >= 10 for car in cars)  # Al menos un auto debe haber ganado
    assert "¡Auto" in winner  # Verifica que el mensaje tiene "¡Auto X ha ganado!"

# ==============================
# Prueba 4: Carrera con una sola vuelta
# ==============================
def test_race_single_turn(monkeypatch):
    """Verifica que la carrera puede terminar en un solo turno si todos avanzan suficiente."""
    
    cars = [Car("Auto 1"), Car("Auto 2")]

    # Simulamos un avance de 10 (garantiza que todos lleguen en un turno)
    monkeypatch.setattr(random, "randint", lambda a, b: 10)

    winner = race(cars, finish_line=10)
    
    assert "¡Auto" in winner  # Verifica que la salida contiene un ganador

