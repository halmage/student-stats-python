"""Clase persona
Autor: Hugo Zorrilla
Fecha: 20/01/2026
Descripcion: Clase persona que representa a una persona con sus atributos y metodos
"""


class PersonaController:
    """Clase persona"""

    def __init__(self, cedula: str, nombre: str, edad: int, genero: str):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
