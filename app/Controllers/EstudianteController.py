"""Clase estudiante

Autor: Hugo Zorrilla
Fecha: 20/01/2026
Descripcion: Clase estudiante que representa a un estudiante con sus atributos
y metodos heredados de la clase persona
"""

# Importaciones clases heredadas
from app.Controllers.PersonaController import PersonaController
from app.Controllers.NotaController import NotaController

# Importaciones clases de base de datos
from app.Models.EstudianteTable import EstudianteTable


class EstudianteController(PersonaController, NotaController):
    """Clase que representa a un estudiante"""

    def __init__(
        self,
        cedula: str = "",
        nombre: str = "",
        edad: int = 0,
        genero: str = "",
        curso: str = "",
        nota: float = 0.0,
    ):
        PersonaController.__init__(self, cedula, nombre, edad, genero)
        NotaController.__init__(self, curso, nota)

    def crear_tabla_estudiantes(self) -> str:
        """
        Crea la tabla de estudiantes

        Returns:
            str: mensaje de estado
        """
        estudiante = EstudianteTable()
        if estudiante.crear_tabla_estudiantes():
            return "Tabla creada exitosamente"
        else:
            return "La tabla ya existe"

    def crear_estudiante(self) -> None:
        """
        Ingresa un estudiante a la base de datos

        Args:
            cedula (str): cedula del estudiante
            nombre (str): nombre del estudiante
            edad (int): edad del estudiante
            genero (str): genero del estudiante
            curso (str): curso del estudiante
            nota (float): nota del estudiante

        Return:
            (bool): True si se creo el estudiante, False si no
        """
        kwargs = {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "edad": self.edad,
            "genero": self.genero,
            "curso": self.curso,
            "nota": self.nota,
        }
        estudiante = EstudianteTable()
        estudiante.crear_estudiante(**kwargs)

    def buscar_estudiante(self, cedula: str) -> bool:
        """
        Busca un estudiante en la base de datos

        Args:
            cedula (str): cedula del estudiante

        Return:
            (bool): True si se encontro el estudiante, False si no
        """
        estudiante = EstudianteTable()
        datos_estudiante = estudiante.buscar_estudiante(cedula)

        if datos_estudiante:
            # Si se encontro el estudiante
            return True
        else:
            # Si no se encontro el estudiante
            return False

    def mostrar_estudiante(self, cedula: str) -> dict | None:
        """
        Busca un estudiante en la base de datos

        Args:
            cedula (str): cedula del estudiante

        Return:
            (bool): True si se encontro el estudiante, False si no
        """
        estudiante = EstudianteTable()
        datos_estudiante = estudiante.buscar_estudiante(cedula)

        if datos_estudiante:
            return {
                "cedula": datos_estudiante[1],
                "nombre": datos_estudiante[2],
                "edad": datos_estudiante[3],
                "genero": datos_estudiante[4],
                "curso": datos_estudiante[5],
                "nota": datos_estudiante[6],
            }
        else:
            return None

    def mostrar_estudiantes(self) -> list[dict] | None:
        """
        Muestra todos los estudiantes de la tabla 'estudiantes'

        Return:
            (list[dict]): lista de estudiantes
        """
        estudiante = EstudianteTable()
        datos_estudiantes = estudiante.mostrar_estudiantes()

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
        else:
            return None

    def eliminar_estudiante(self, cedula: str) -> None:
        """
        Elimina un estudiante de la tabla 'estudiantes'

        Args:
            cedula (str): cedula del estudiante
        """
        estudiante = EstudianteTable()
        estudiante.eliminar_estudiante(cedula)

    def estudiantes_masculino(self) -> list:
        """
        Lista de estudiantes masculinos

        Return:
            (list): lista de estudiantes masculinos
        """
        estudiante = EstudianteTable()
        datos_estudiantes = estudiante.estudiantes_masculino()

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
        else:
            return None

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
        else:
            return None

    def cantidad_estudiantes(self) -> int:
        """
        Suma de estudiantes femenino y masculino

        Return:
            (int): suma de estudiantes femenino y masculino
        """
        estudiante = EstudianteTable()
        return len(estudiante.mostrar_estudiantes())

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
        else:
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
        else:
            return None
