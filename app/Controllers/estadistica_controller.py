"""Clase EstadisticaController

Autor: Hugo Zorrilla
Fecha: 20/01/2026
Descripcion: Clase EstadisticaController que representa a un estadistica
con sus atributos y metodos heredados de la clase persona
"""

# Importaciones clases heredadas
from app.Controllers.estudiante_controller import EstudianteController
from app.Models.estudiante_table import EstudianteTable


class EstadisticaController(EstudianteController):
    """Clase que representa a un estadistica"""

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

    def estudiantes_femenino(self) -> list:
        """
        Lista de estudiantes femeninos

        Return:
            (list): lista de estudiantes femeninos
        """
        estudiante = EstudianteTable()
        datos_estudiantes = estudiante.estudiantes_femenino()

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
        estudiante = EstudianteTable()
        if estudiante.mostrar_estudiantes():
            return len(estudiante.mostrar_estudiantes())
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
        estudiante = EstudianteTable()
        datos_estudiantes = estudiante.estudiantes_reprobados()

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
        estudiante = EstudianteTable()
        datos_estudiantes = estudiante.estudiantes_aprobados()

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
