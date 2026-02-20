"""
Clase NotaController

MÓDULO: nota_controller.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN:
Es una clase llamada NotaController que representa a una nota con
sus atributos de curso y calificación.

* Gestión de Datos Académicos: Define la estructura básica para
manejar la información de los cursos y las notas numéricas de los estudiantes.

* Validación de Cursos: Implementa la lógica para verificar que los
cursos ingresados pertenezcan a las opciones permitidas por el sistema
(como matemáticas, ciencias, historia, geografía o biología).

* Validación de Calificaciones: Asegura que las notas ingresadas estén
dentro de un rango válido (de 0 a 10) y que cumplan con el formato
numérico correcto.

* Soporte de Herencia: Funciona como una clase base que es heredada
por otros controladores (como EstudianteController) para integrar la
lógica de calificaciones en el perfil completo del alumno.
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

    def evaluacion(self, nota) -> str:
        """Evaluacion de la nota

        Returns:
            str: evaluacion de la nota
        """
        if 5 >= nota <= 7:
            return "Aprobado"
        if nota > 7:
            return "Excelente"
        if nota < 5:
            return "Reprobado"
        return None
