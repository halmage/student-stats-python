"""Clase EstudianteController

Autor: Hugo Zorrilla
Fecha: 20/01/2026
Descripcion: Clase EstudianteController que representa a un estudiante
con sus atributos y metodos heredados de la clase persona
"""

# Importaciones clases heredadas
from app.Controllers.persona_controller import PersonaController
from app.Controllers.nota_controller import NotaController

# Importaciones clases de base de datos
from app.Models.estudiante_table import EstudianteTable


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
        return "La tabla ya existe"

    def eliminar_tabla_estudiantes(self) -> str:
        """
        Elimina la tabla de estudiantes

        Returns:
            str: mensaje de estado
        """
        estudiante = EstudianteTable()
        if estudiante.eliminar_tabla_estudiantes():
            return "Tabla eliminada exitosamente"
        return "La tabla no existe"

    def crear_estudiante(self) -> None:
        """Ingresa un estudiante a la base de datos"""

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
        return ""
