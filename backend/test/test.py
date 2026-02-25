import sys
import os
# Añadir el directorio superior al path para poder importar main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import generate_username

def test_generate_username_logic():
    """
    Valida la regla de negocio: primera letra + apellido y manejo de duplicados.
    """
    used = set()
    
    # Caso 1: Generación básica
    assert generate_username.generate_username("John Doe", used) == "jdoe"
    
    # Caso 2: Manejo de prefijos (Mr, Dr, etc.)
    assert generate_username.generate_username("Dr. James Smith", used) == "jsmith"
    assert generate_username.generate_username("Ms. Anna Lee", used) == "alee"
    assert generate_username.generate_username("Mr. Robert Brown", used) == "rbrown"
    assert generate_username.generate_username("Mrs. Emily Davis", used) == "edavis"
    
    # Caso 3: Manejo de duplicidad
    # 'jdoe' ya existe en 'used', así que el siguiente debe ser 'jdoe1', lo mismo para el siguiente 'jdoe2'
    assert generate_username.generate_username("Johana Doe", used) == "jdoe1"
    assert generate_username.generate_username("Johana Doe", used) == "jdoe2"
    
    # Caso 4: Limpieza de caracteres y minúsculas
    assert generate_username.generate_username("ALICE-MARIE WONDERLAND", used) == "awonderland"
    assert generate_username.generate_username("José Alejandro Gutiérrez", used) == "jgutierrez"
    assert generate_username.generate_username("Íñigo Montoya", used) == "imontoya"
    assert generate_username.generate_username("Dr. Ramón Nuñez Jr.", used) == "rnunez"

def test_generate_username_multiple_collisions():
    """Verifica que el contador avance correctamente"""
    used = {"jdoe", "jdoe1", "jdoe2"}
    assert generate_username.generate_username("Jim Doe", used) == "jdoe3"
    

def test_generate_username_edge_cases():
    """Prueba casos con nombres atípicos"""
    used = set()
    
    # Caso 1: Nombre sin apellido
    assert generate_username.generate_username("Madonna", used) == "m"
    
    # Caso 2: Nombre con múltiples espacios
    assert generate_username.generate_username("   John   Doe   ", used) == "jdoe"
    
    # Caso 3: Nombre con caracteres especiales
    assert generate_username.generate_username("Jean-Luc Picard", used) == "jpicard"