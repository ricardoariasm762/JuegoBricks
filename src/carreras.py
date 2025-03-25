import random

class Car:
    """Clase para representar un auto de carrera."""
    def __init__(self, name):
        self.name = name
        self.position = 0

    def advance(self):
        """El auto avanza una distancia aleatoria en cada turno."""
        self.position += random.randint(1, 6)

def race(cars, finish_line=20):
    """Simula una carrera hasta la meta."""
    while True:
        for car in cars:
            car.advance()
            print(f"{car.name} está en la posición {car.position}")
            if car.position >= finish_line:
                return f"\n¡{car.name} ha ganado la carrera!"

# Ejemplo de uso
cars = [Car("Auto 1"), Car("Auto 2"), Car("Auto 3")]
print(race(cars))
