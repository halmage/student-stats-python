"""
Clase EstadisticaController

MÓDULO: estadistica_controller.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN:
Es una clase llamada EstadisticaController que representa a una
estadística con sus atributos y métodos heredados de la clase EstudianteController.

* Heredar de EstudianteController para manejar los datos básicos del estudiante.

* Realizar el cálculo del promedio general de las notas de los estudiantes
registrados en la base de datos.

* Determinar el porcentaje de estudiantes que han aprobado o reprobado
según sus calificaciones.

* Evaluar el estado académico individual (Aprobado/Reprobado) de un estudiante
basándose en su nota.
"""

# Importaciones clases heredadas
from app.Controllers.estudiante_controller import EstudianteController
from app.Models.estudiante_table import EstudianteTable


class EstadisticaController(EstudianteController):
    """Clase que representa el controlador de estadísticas"""

    def __init__(
        self,
        cedula: str = "",
        nombre: str = "",
        edad: int = 0,
        genero: str = "",
        curso: str = "",
        nota: float = 0.0,
    ):
        EstudianteController.__init__(self, cedula, nombre, edad, genero, curso, nota)
        self.estudiante_table = EstudianteTable()

    def estudiantes_femenino(self) -> list:
        """
        Lista de estudiantes femeninos

        Return:
            (list): lista de estudiantes femeninos
        """
        datos_estudiantes = self.estudiante_table.estudiantes_femenino()

        if datos_estudiantes:
            return [
                {
                    "cedula": datos_estudiante[1],
                    "nombre": datos_estudiante[2],
                    "edad": datos_estudiante[3],
                    "genero": datos_estudiante[4],
                    "curso": datos_estudiante[5],
                    "nota": datos_estudiante[6],
                }
                for datos_estudiante in datos_estudiantes
            ]
        return ""

    def cantidad_estudiantes(self) -> int:
        """
        Suma de estudiantes femenino y masculino

        Return:
            (int): suma de estudiantes femenino y masculino
        """
        if self.estudiante_table.mostrar_estudiantes():
            return len(self.estudiante_table.mostrar_estudiantes())
        return 0

    def porcentaje_estudiantes_masculinos(self) -> float:
        """
        Porcentaje de estudiantes masculinos en el colegio

        Return:
            (float): porcentaje de estudiantes masculinos
        """
        total_estudiantes = self.cantidad_estudiantes()
        cantidad_estudiantes_masculino = len(self.estudiantes_masculino())
        return (cantidad_estudiantes_masculino * 100) / total_estudiantes

    def porcentaje_estudiantes_femeninos(self) -> float:
        """
        Porcentaje de estudiantes femeninos en el colegio

        Return:
            (float): porcentaje de estudiantes femeninos
        """
        total_estudiantes = self.cantidad_estudiantes()
        cantidad_estudiantes_femenino = len(self.estudiantes_femenino())
        return (cantidad_estudiantes_femenino * 100) / total_estudiantes

    def porcentaje_total_estudiantes(self) -> float:
        """
        Porcentaje total de estudiantes en el colegio

        Return:
            (float): porcentaje total de estudiantes
        """
        total_estudiantes = self.cantidad_estudiantes()
        return (total_estudiantes * 100) / total_estudiantes

    def estudiantes_reprobados(self) -> list:
        """
        Lista de estudiantes reprobados

        Return:
            (list): lista de estudiantes reprobados
        """
        datos_estudiantes = self.estudiante_table.estudiantes_reprobados()

        if datos_estudiantes:
            return [
                {
                    "cedula": datos_estudiante[1],
                    "nombre": datos_estudiante[2],
                    "edad": datos_estudiante[3],
                    "genero": datos_estudiante[4],
                    "curso": datos_estudiante[5],
                    "nota": datos_estudiante[6],
                }
                for datos_estudiante in datos_estudiantes
            ]
        return None

    def estudiantes_aprobados(self) -> list:
        """
        Lista de estudiantes aprobados

        Return:
            (list): lista de estudiantes aprobados
        """
        datos_estudiantes = self.estudiante_table.estudiantes_aprobados()

        if datos_estudiantes:
            return [
                {
                    "cedula": datos_estudiante[1],
                    "nombre": datos_estudiante[2],
                    "edad": datos_estudiante[3],
                    "genero": datos_estudiante[4],
                    "curso": datos_estudiante[5],
                    "nota": datos_estudiante[6],
                }
                for datos_estudiante in datos_estudiantes
            ]
        return None
