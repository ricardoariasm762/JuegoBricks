import pytest
from datetime import datetime, timedelta
from src.utilidades import current_time, days_between, add_days

# ==============================
# Prueba 1: current_time()
# ==============================
def test_current_time():
    """Verifica que current_time devuelve una fecha con el formato correcto."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assert isinstance(current_time(), str)
    assert current_time()[:10] == now[:10]  # Compara solo la parte de la fecha

# ==============================
# Prueba 2: days_between()
# ==============================
@pytest.mark.parametrize(
    "date1, date2, expected",
    [
        ("2024-03-01", "2024-03-10", 9),
        ("2024-01-01", "2024-01-01", 0),
        ("2023-12-31", "2024-01-01", 1),
        ("2022-05-15", "2023-05-15", 365),
    ],
)
def test_days_between(date1, date2, expected):
    """Verifica que days_between calcula correctamente la diferencia en días."""
    assert days_between(date1, date2) == expected

# ==============================
# Prueba 3: add_days()
# ==============================
@pytest.mark.parametrize(
    "date_str, days, expected",
    [
        ("2024-03-01", 10, "2024-03-11"),
        ("2024-02-28", 1, "2024-02-29"),  # Año bisiesto
        ("2023-12-31", 1, "2024-01-01"),
        ("2024-01-01", -1, "2023-12-31"),  # Retroceder un día
        ("2024-06-15", 30, "2024-07-15"),
    ],
)
def test_add_days(date_str, days, expected):
    """Verifica que add_days suma días correctamente a una fecha."""
    assert add_days(date_str, days) == expected
