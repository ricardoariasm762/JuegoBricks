def reverse_string(s):
    """Devuelve la cadena invertida."""
    return s[::-1]

def is_palindrome(s):
    """Verifica si una cadena es un palíndromo."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_vowels(s):
    """Cuenta la cantidad de vocales en una cadena."""
    return sum(1 for char in s.lower() if char in "aeiou")

def capitalize_words(s):
    """Convierte la primera letra de cada palabra en mayúscula."""
    return s.title()
