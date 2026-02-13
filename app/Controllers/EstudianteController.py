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

    def eliminar_tabla_estudiantes(self) -> None:
        """
        Elimina la tabla de estudiantes

        Returns:
            str: mensaje de estado
        """
        estudiante = EstudianteTable()
        if estudiante.eliminar_tabla_estudiantes():
            return "Tabla eliminada exitosamente"

    def validar_cedula(self, cedula: str) -> None:
        """
        Valida la cedula del estudiante

        Returns:
            (bool): True si la cedula es valida, False si no
        """

        if self.buscar_estudiante(cedula):
            return "Error: La cedula ya existe"

        if cedula == "":
            return "Error: La cedula no puede estar vacia"

        if not cedula.isdigit() or int(cedula) < 0 or len(cedula) != 8:
            return "Error: La cedula tiene que ser un numero positivo de 8 digitos"

    def validar_nombre(self, nombre: str) -> None:
        """
        Valida el nombre del estudiante

        Returns:
            (bool): True si el nombre es valido, False si no
        """
        if nombre == "":
            return "Error: El nombre no puede estar vacio"
        if not nombre.isalpha():
            return "Error: El nombre tiene que ser un caracter"
        if len(nombre) < 3:
            return "Error: El nombre debe tener al menos 3 caracteres"
        if len(nombre) > 20:
            return "Error: El nombre debe tener menos de 20 caracteres"

    def validar_edad(self, edad: str) -> None:
        """
        Valida la edad del estudiante

        Returns:
            (bool): True si la edad es valida, False si no
        """
        if edad == "":
            return "La edad no puede estar vacia"
        if not edad.isdigit():
            return "La edad debe ser un numero positivo"
        if int(edad) < 0 or int(edad) not in range(10, 18):
            return "La edad debe ser un numero positivo entre 10 y 17"

    def validar_genero(self, genero: str) -> None:
        """
        Valida el genero del estudiante

        Returns:
            (bool): True si el genero es valido, False si no
        """
        if genero == "":
            return "El genero no puede estar vacio"
        elif genero not in ["femenino", "masculino"]:
            return "El genero debe ser Masculino o Femenino"

    def validar_curso(self, curso: str) -> None:
        """
        Valida el curso del estudiante

        Returns:
            (bool): True si el curso es valido, False si no
        """
        if curso == "":
            return "El curso no puede estar vacio"
        elif not curso.isalpha() or curso not in [
            "matematicas",
            "ciencias",
            "historia",
            "geografia",
            "biologia",
        ]:
            return "\nError: el dato no es caracter o no es un curso del colegio"

    def validar_nota(self, nota: float) -> None:
        """
        Valida la nota del estudiante

        Returns:
            (bool): True si la nota es valida, False si no
        """
        if nota == "":
            return "La nota no puede estar vacia"
        elif not nota.isdigit() or float(nota) < 0 or float(nota) > 10:
            return "La nota debe ser un numero entre 0 y 10"

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
            return ""

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
        else:
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
