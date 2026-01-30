import sqlite3


class EstudianteTable:
    """Clase EstudianteTable"""

    def __init__(self):
        self.conexion = sqlite3.connect("app/Models/colegio.db")

    def create_database(self):
        """
        Crear la base de datos si no existe y crear la tabla 'estudiantes'
        con los campos id, cedula, nombre, edad, genero, curso y nota
        """
        try:
            self.conexion.execute(
                """
                create table estudiantes (
                                    id integer primary key autoincrement,
                                    cedula text not null,
                                    nombre text not null,
                                    edad integer not null,
                                    genero text not null,
                                    curso text not null,
                                    nota float not null
                                )"""
            )
            self.conexion.close()
        except sqlite3.OperationalError:
            self.conexion.close()

    def crear_estudiante(self, **kwargs):
        """
        Insertar un estudiante en la tabla 'estudiantes'

        Args:
            cedula (str): Cedula del estudiante
            nombre (str): Nombre del estudiante
            edad (int): Edad del estudiante
            genero (str): Genero del estudiante
            curso (str): Curso del estudiante
            nota (float): Nota del estudiante
        """
        try:
            self.conexion.execute(
                """
                insert into estudiantes (cedula, nombre, edad, genero, curso, nota) values (?, ?, ?, ?, ?, ?)
                """,
                (
                    kwargs["cedula"],
                    kwargs["nombre"],
                    kwargs["edad"],
                    kwargs["genero"],
                    kwargs["curso"],
                    kwargs["nota"],
                ),
            )
            self.conexion.commit()
            self.conexion.close()
        except sqlite3.OperationalError:
            self.conexion.close()

    def buscar_estudiante(self, cedula: str):
        """
        Buscar un estudiante en la tabla 'estudiantes'

        Args:
            cedula (str): Cedula del estudiante
        """
        try:
            cursor = self.conexion.execute(
                """
                select * from estudiantes where cedula = ?
                """,
                (cedula,),
            )

            return cursor.fetchone()
        except sqlite3.OperationalError:
            self.conexion.close()

    def mostrar_estudiantes(self):
        """
        Mostrar todos los estudiantes de la tabla 'estudiantes'
        """
        try:
            cursor = self.conexion.execute(
                """
                select * from estudiantes
                """
            )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            self.conexion.close()

    def eliminar_estudiante(self, cedula: str):
        """
        Eliminar un estudiante de la tabla 'estudiantes'

        Args:
            cedula (str): Cedula del estudiante
        """
        try:
            self.conexion.execute(
                """
                delete from estudiantes where cedula = ?
                """,
                (cedula,),
            )
            self.conexion.commit()
            self.conexion.close()
        except sqlite3.OperationalError:
            self.conexion.close()

    def estudiantes_masculino(self) -> int:
        """
        Cantidad de estudiantes masculino

        Return:
            (int): cantidad de estudiantes masculino
        """
        try:
            cursor = self.conexion.execute(
                """
                select * from estudiantes where genero = 'masculino'
                """
            )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            self.conexion.close()

    def estudiantes_femenino(self) -> int:
        """
        Cantidad de estudiantes femenino

        Return:
            (int): cantidad de estudiantes femenino
        """
        try:
            cursor = self.conexion.execute(
                """
                select * from estudiantes where genero = 'femenino'
                """
            )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            self.conexion.close()

    def estudiantes_reprobados(self) -> int:
        """
        Cantidad de estudiantes reprobados

        Return:
            (int): cantidad de estudiantes reprobados
        """
        try:
            cursor = self.conexion.execute(
                """
                select * from estudiantes where nota < 5
                """
            )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            self.conexion.close()

    def estudiantes_aprobados(self) -> int:
        """
        Cantidad de estudiantes aprobados

        Return:
            (int): cantidad de estudiantes aprobados
        """
        try:
            cursor = self.conexion.execute(
                """
                select * from estudiantes where nota >= 5
                """
            )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            self.conexion.close()
