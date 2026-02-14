"""
Clase Nota
Autor: Hugo Zorrilla
Fecha: 21/01/2026
Descripcion: Clase Nota que representa a una nota con sus atributos
y metodos
"""


class NotaController:
    """Clase Nota"""

    def __init__(self, curso: str = "", nota: float = 0.0):
        """Constructor de la clase Nota"""
        self.curso = curso
        self.nota = nota

    def validar_curso(self, curso: str) -> str:
        """
        Valida el curso del estudiante

        Returns:
            str: mensaje de estado
        """
        if curso == "":
            return "El curso no puede estar vacio"
        if not curso.isalpha() or curso not in [
            "matematicas",
            "ciencias",
            "historia",
            "geografia",
            "biologia",
        ]:
            return "\nError: el dato no es caracter o no es un curso del colegio"
        return None

    def validar_nota(self, nota: float) -> str:
        """
        Valida la nota del estudiante

        Returns:
            str: mensaje de estado
        """
        if nota == "":
            return "La nota no puede estar vacia"
        if not nota.isdigit() or float(nota) < 0 or float(nota) > 10:
            return "La nota debe ser un numero entre 0 y 10"
        return None

    def evaluacion(self, nota: float) -> str:
        """Evaluacion de la nota

        Returns:
            str: evaluacion de la nota
        """
        if self.nota >= 5 and self.nota <= 7:
            return "Aprobado"
        if self.nota > 7:
            return "Excelente"
        if self.nota < 5:
            return "Reprobado"
        return None
