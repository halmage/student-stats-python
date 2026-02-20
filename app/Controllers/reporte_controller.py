"""
Clase ReporteController

MÓDULO: reporte_controller.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN:
Es una clase llamada ReporteController que se encarga de la generación y
gestión de informes externos basados en los datos del sistema.

* Herencia Múltiple Estratégica: Hereda de EstadisticaController y
EstudianteController para tener acceso tanto a los métodos de cálculo
estadístico como a la gestión de la lista de alumnos.

* Generación de Reportes en CSV: Implementa la lógica para extraer la
información de la base de datos y convertirla a un formato de valores
separados por comas (CSV), permitiendo que los datos sean legibles en
herramientas como Excel.

* Gestión de Almacenamiento: Define y gestiona la ruta de salida de los
archivos (usualmente en una carpeta de activos o reportes), asegurando
que los informes se guarden de manera organizada.

* Automatización de Análisis: Permite exportar de forma masiva el estado
académico de los estudiantes (promedios, aprobados y reprobados),
facilitando la toma de decisiones administrativas sin necesidad de
consultar el sistema manualmente.
"""

import os


# Importaciones clases heredadas
from app.Controllers.estudiante_controller import EstudianteController
from app.Controllers.estadistica_controller import EstadisticaController


class ReporteController(EstadisticaController, EstudianteController):
    """Clase que representa a un reporte"""

    SOURCE_DIR = "app/assets/reports/"

    def __init__(
        self,
        cedula: str = "",
        nombre: str = "",
        edad: int = 0,
        genero: str = "",
        curso: str = "",
        nota: float = 0.0,
    ):
        EstadisticaController.__init__(self, cedula, nombre, edad, genero, curso, nota)
        EstudianteController.__init__(self, cedula, nombre, edad, genero, curso, nota)

    def reporte_listado_estudiantes(self) -> str:
        """
        Genera un reporte general de los estudiantes

        Returns:
            str: reporte general
        """
        file_name = "reporte_listado_estudiantes.csv"
        file_path = os.path.join(self.SOURCE_DIR, file_name)

        estudiantes = self.mostrar_estudiantes()
        if not estudiantes:
            # No hay estudiantes para generar el reporte
            return "No hay estudiantes para generar el reporte"

        # Crear reporte general
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Cedula,Nombre,Edad,Genero,Curso,Nota\n")
            for estudiante in estudiantes:
                f.write(
                    f"{estudiante['cedula']},{estudiante['nombre']},{estudiante['edad']},{estudiante['genero']},{estudiante['curso']},{estudiante['nota']}\n"
                )
        return "Reporte generado exitosamente"

    def reporte_estudiantes_aprobados_reprobados(self) -> str:
        """
        Genera un reporte de estudiantes aprobados y reprobados

        Returns:
            str: reporte de estudiantes aprobados y reprobados
        """
        file_name: str = "reporte_estudiantes_aprobados_reprobados.csv"
        file_path: str = os.path.join(self.SOURCE_DIR, file_name)

        estudiantes = self.mostrar_estudiantes()
        if not estudiantes:
            # No hay estudiantes para generar el reporte
            return "No hay estudiantes para generar el reporte"

        # Crear reporte de estudiantes aprobados y reprobados
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Cedula,Nombre,Edad,Genero,Curso,Nota,Estado\n")
            for estudiante in estudiantes:
                estado = self.evaluacion(estudiante["nota"])
                f.write(
                    f"{estudiante['cedula']},{estudiante['nombre']},{estudiante['edad']},{estudiante['genero']},{estudiante['curso']},{estudiante['nota']},{estado}\n"
                )
        return "Reporte generado exitosamente"

    def reporte_estudiantes_aprobados(self) -> str:
        """
        Genera un reporte de estudiantes aprobados

        Returns:
            str: reporte de estudiantes aprobados
        """
        file_name: str = "reporte_estudiantes_aprobados.csv"
        file_path: str = os.path.join(self.SOURCE_DIR, file_name)

        estudiantes = self.estudiantes_aprobados()
        if not estudiantes:
            # No hay estudiantes para generar el reporte
            return "No hay estudiantes aprobados para generar el reporte"

        # Crear reporte de estudiantes aprobados
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Cedula,Nombre,Edad,Genero,Curso,Nota\n")
            for estudiante in estudiantes:
                f.write(
                    f"{estudiante['cedula']},{estudiante['nombre']},{estudiante['edad']},{estudiante['genero']},{estudiante['curso']},{estudiante['nota']}\n"
                )
        return "Reporte generado exitosamente"

    def reporte_estudiantes_reprobados(self) -> str:
        """
        Genera un reporte de estudiantes reprobados

        Returns:
            str: reporte de estudiantes reprobados
        """
        file_name: str = "reporte_estudiantes_reprobados.csv"
        file_path: str = os.path.join(self.SOURCE_DIR, file_name)

        estudiantes = self.estudiantes_reprobados()
        if not estudiantes:
            # No hay estudiantes para generar el reporte
            return "No hay estudiantes reprobados para generar el reporte"

        # Crear reporte de estudiantes reprobados
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Cedula,Nombre,Edad,Genero,Curso,Nota\n")
            for estudiante in estudiantes:
                f.write(
                    f"{estudiante['cedula']},{estudiante['nombre']},{estudiante['edad']},{estudiante['genero']},{estudiante['curso']},{estudiante['nota']}\n"
                )
        return "Reporte generado exitosamente"

    def reporte_estudiantes_por_curso(self, curso: str) -> str:
        """
        Genera un reporte de estudiantes por curso

        Returns:
            str: reporte de estudiantes por curso
        """
        file_name: str = f"reporte_estudiantes_{curso}.csv"
        file_path: str = os.path.join(self.SOURCE_DIR, file_name)

        estudiantes = self.mostrar_estudiantes_por_curso(curso)
        if not estudiantes:
            # No hay estudiantes para generar el reporte
            return f"No hay estudiantes en el curso {curso}"

        # Crear reporte de estudiantes por curso
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Cedula,Nombre,Edad,Genero,Curso,Nota\n")
            for estudiante in estudiantes:
                f.write(
                    f"{estudiante['cedula']},{estudiante['nombre']},{estudiante['edad']},{estudiante['genero']},{estudiante['curso']},{estudiante['nota']}\n"
                )
        return f"Reporte generado exitosamente en el curso {curso}"
