"""
Clase PersonaController

MÓDULO: persona_controller.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN:
Es una clase llamada PersonaController que representa a una
persona con sus atributos básicos de identificación.


* Definición de Atributos Base: Establece los datos fundamentales
que toda persona en el sistema debe tener: cédula, nombre, apellido, edad y género.

* Lógica de Validación de Identidad: Implementa métodos para asegurar
que la cédula sea un dato numérico y que el género corresponda a las opciones
válidas (Masculino o Femenino).

* Validación de Datos Personales: Incluye lógica para verificar que la edad
esté en un rango lógico (de 0 a 100 años) y que el nombre cumpla con el formato
de texto adecuado.

* Clase Base para Herencia: Sirve como el pilar fundamental del cual heredan otros
controladores (como EstudianteController y EstadisticaController), permitiendo que
el sistema mantenga la consistencia de los datos personales en todos sus módulos.
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
