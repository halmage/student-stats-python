"""
Clase Nota
Autor: Hugo Zorrilla
Fecha: 21/01/2026
"""


class NotaController:
    """Clase Nota"""

    def __init__(self, curso, nota):
        """Constructor de la clase Nota"""
        self.curso = curso
        self.nota = nota

    def evaluacion(self) -> str:
        """Evaluacion de la nota"""
        if self.nota >= 5 and self.nota <= 7:
            return "Aprobado"
        elif self.nota > 7:
            return "Excelente"
        elif self.nota < 5:
            return "Reprobado"
