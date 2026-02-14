"""
Tabla EstudianteTable: tabla de base de datos para el control de estudiantes
"""

import sqlite3
import os

# Ruta relativa
ARCHIVO_RELATIVO: str = "colegio.db"

# Convertir a absoluta
RUTA_ABSOLUTA: str = os.path.abspath(ARCHIVO_RELATIVO)


class EstudianteTable:
    """Clase EstudianteTable"""

    def __init__(self) -> None:
        with sqlite3.connect(RUTA_ABSOLUTA) as conexion:
            self.conexion = conexion

    def crear_tabla_estudiantes(self) -> bool:
        """
        Crear la tabla 'estudiantes'
        con los campos id, cedula, nombre, edad, genero, curso y nota

        Returns:
            bool: True si la tabla fue creada, False si ya existe
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
            self.conexion.commit()
            return True
        except sqlite3.OperationalError:
            return False

    def eliminar_tabla_estudiantes(self) -> None:
        """
        Eliminar la tabla 'estudiantes'
        """
        try:
            self.conexion.execute(
                """
                drop table estudiantes
                """
            )
            self.conexion.commit()
        except sqlite3.OperationalError:
            return []

    def crear_estudiante(self, **kwargs) -> None:
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
                insert into estudiantes (cedula, nombre, edad, genero, curso, nota)
                values (?, ?, ?, ?, ?, ?)
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
        except sqlite3.OperationalError:
            return []

    def buscar_estudiante(self, cedula: str) -> tuple:
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
            return []

    def mostrar_estudiantes(self) -> list:
        """
        Mostrar todos los estudiantes de la tabla 'estudiantes'

        Returns:
            list: lista de estudiantes
        """
        try:
            cursor = self.conexion.execute(
                """
                select * from estudiantes
                """
            )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            return []

    def mostrar_estudiantes_por_curso(self, curso: str) -> list:
        """
        Mostrar todos los estudiantes de la tabla 'estudiantes'

        Args:
            curso (str): Curso del estudiante

        Returns:
            list: lista de estudiantes
        """
        try:
            cursor = self.conexion.execute(
                """
                select * from estudiantes where curso = ?
                """,
                (curso,),
            )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            return []

    def eliminar_estudiante(self, cedula: str) -> None:
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
        except sqlite3.OperationalError:
            return []

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
            return []

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
            return []

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
            return []

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
            return []
