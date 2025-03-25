import pytest
from src.text import read_file, write_file, append_to_file

# ==============================
# Prueba 1: write_file()
# ==============================
def test_write_file(tmp_path):
    """Verifica que write_file crea y escribe contenido en un archivo."""
    file_path = tmp_path / "test_file.txt"
    content = "Hola, mundo!"

    write_file(file_path, content)

    assert file_path.exists()  # Verifica que el archivo fue creado
    assert file_path.read_text(encoding="utf-8") == content  # Verifica contenido

# ==============================
# Prueba 2: read_file()
# ==============================
def test_read_file(tmp_path):
    """Verifica que read_file lee correctamente el contenido de un archivo."""
    file_path = tmp_path / "test_file.txt"
    content = "Texto de prueba"

    file_path.write_text(content, encoding="utf-8")  # Crea archivo con contenido

    assert read_file(file_path) == content  # Verifica lectura correcta

# ==============================
# Prueba 3: append_to_file()
# ==============================
def test_append_to_file(tmp_path):
    """Verifica que append_to_file agrega contenido al final de un archivo."""
    file_path = tmp_path / "test_file.txt"
    initial_content = "Línea 1"
    additional_content = "Línea 2"

    file_path.write_text(initial_content + "\n", encoding="utf-8")  # Archivo inicial
    append_to_file(file_path, additional_content)  # Agrega línea

    expected_content = "Línea 1\nLínea 2\n"
    assert file_path.read_text(encoding="utf-8") == expected_content  # Verifica

# ==============================
# Prueba 4: read_file con archivo inexistente
# ==============================
def test_read_file_not_found():
    """Verifica que leer un archivo inexistente lanza un error."""
    with pytest.raises(FileNotFoundError):
        read_file("archivo_inexistente.txt")
