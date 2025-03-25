import pytest
from src.palindromo import reverse_string, is_palindrome, count_vowels, capitalize_words

# ==============================
# Prueba 1: reverse_string()
# ==============================
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("hola", "aloh"),
        ("Python", "nohtyP"),
        ("", ""),
        ("12345", "54321"),
        ("Anita", "atinA"),
    ],
)
def test_reverse_string(input_str, expected):
    """Verifica que reverse_string invierte correctamente la cadena."""
    assert reverse_string(input_str) == expected

# ==============================
# Prueba 2: is_palindrome()
# ==============================
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("reconocer", True),
        ("Anita lava la tina", True),  # Palíndromo con espacios
        ("Python", False),
        ("12321", True),
        ("hola", False),
    ],
)
def test_is_palindrome(input_str, expected):
    """Verifica que is_palindrome identifica correctamente los palíndromos."""
    assert is_palindrome(input_str) == expected

# ==============================
# Prueba 3: count_vowels()
# ==============================
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("hola", 2),
        ("PYTHON", 1),
        ("murcielago", 5),
        ("", 0),
        ("bcdfg", 0),  # Sin vocales
    ],
)
def test_count_vowels(input_str, expected):
    """Verifica que count_vowels cuenta correctamente las vocales en una cadena."""
    assert count_vowels(input_str) == expected

# ==============================
# Prueba 4: capitalize_words()
# ==============================
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("hola mundo", "Hola Mundo"),
        ("python es genial", "Python Es Genial"),
        ("PYTHON", "Python"),
        ("123 abc", "123 Abc"),
        ("", ""),
    ],
)
def test_capitalize_words(input_str, expected):
    """Verifica que capitalize_words convierte correctamente las palabras a mayúscula inicial."""
    assert capitalize_words(input_str) == expected
