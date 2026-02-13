"""Clase persona
Autor: Hugo Zorrilla
Fecha: 20/01/2026
Descripcion: Clase persona que representa a una persona con sus atributos y metodos
"""


class PersonaController:
    """Clase persona"""

    def __init__(
        self, cedula: str = "", nombre: str = "", edad: int = 0, genero: str = ""
    ):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def validar_cedula(self, cedula: str) -> str:
        """
        Valida la cedula del estudiante

        Returns:
            str: mensaje de estado
        """

        if cedula == "":
            return "Error: La cedula no puede estar vacia"
        if not cedula.isdigit() or int(cedula) < 0 or len(cedula) != 8:
            return "Error: La cedula tiene que ser un numero positivo de 8 digitos"
        return None

    def validar_nombre(self, nombre: str) -> str:
        """
        Valida el nombre del estudiante

        Returns:
            str: mensaje de estado
        """
        if nombre == "":
            return "Error: El nombre no puede estar vacio"
        if not nombre.isalpha():
            return "Error: El nombre tiene que ser un caracter"
        if len(nombre) < 3:
            return "Error: El nombre debe tener al menos 3 caracteres"
        if len(nombre) > 20:
            return "Error: El nombre debe tener menos de 20 caracteres"
        return None

    def validar_edad(self, edad: str) -> str:
        """
        Valida la edad del estudiante

        Returns:
            str: mensaje de estado
        """
        if edad == "":
            return "La edad no puede estar vacia"
        if not edad.isdigit():
            return "La edad debe ser un numero positivo"
        if int(edad) < 0 or int(edad) not in range(10, 18):
            return "La edad debe ser un numero positivo entre 10 y 17"
        return None

    def validar_genero(self, genero: str) -> str:
        """
        Valida el genero del estudiante

        Returns:
            str: mensaje de estado
        """
        if genero == "":
            return "El genero no puede estar vacio"
        if genero not in ["femenino", "masculino"]:
            return "El genero debe ser femenino o masculino"
        return None
