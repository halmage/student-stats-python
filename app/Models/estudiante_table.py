"""
Clase EstudianteTable

MÓDULO: estudiante_table.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN:
        Define la creación y el esquema de la tabla 'estudiantes'.
        Implementa las restricciones de integridad (Unique, Not Null).
"""

import sqlite3
import os
# from faker import Faker


class EstudianteTable:
    """Clase EstudianteTable"""

    # Ruta relativa
    NOMBRE_BASE_DE_DATOS: str = "colegio.db"

    # Convertir a absoluta
    RUTA_ABSOLUTA: str = os.path.abspath(NOMBRE_BASE_DE_DATOS)

    def crear_tabla_estudiantes(self) -> bool:
        """
        Crear la tabla 'estudiantes'
        con los campos id, cedula, nombre, edad, genero, curso y nota

        Returns:
            bool: True si la tabla fue creada, False si ya existe
        """
        try:
            fake = Faker(locale="es_ES")
            with sqlite3.connect(self.RUTA_ABSOLUTA) as conexion:
                conexion.execute(
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
                # Generar e insertar 110 registros falsos
            # for _ in range(10):
            #     cedula = fake.random_int(min=10000000, max=99999999)
            #     nombre = fake.first_name().lower()
            #     edad = fake.random_int(min=10, max=17)
            #     genero = fake.random_element(elements=("masculino", "femenino"))
            #     curso = fake.random_element(
            #         elements=(
            #             "matematicas",
            #             "ciencias",
            #             "historia",
            #             "geografia",
            #             "biologia",
            #         )
            #     )
            #     nota = fake.random_int(min=1, max=10)
            #     conexion.execute(
            #         """
            #         insert into estudiantes (cedula, nombre, edad, genero, curso, nota)
            #         values (?, ?, ?, ?, ?, ?)""",
            #         (cedula, nombre, edad, genero, curso, nota),
            #     )
            # conexion.commit()
            return True
        except sqlite3.OperationalError:
            return False

    def eliminar_tabla_estudiantes(self) -> None:
        """
        Eliminar la tabla 'estudiantes'
        """
        try:
            if os.path.exists(self.NOMBRE_BASE_DE_DATOS):
                os.remove(self.NOMBRE_BASE_DE_DATOS)
        except Exception as e:
            print(f"\nError al intentar eliminar la base de datos: {e}")

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
            with sqlite3.connect(self.RUTA_ABSOLUTA) as conexion:
                conexion.execute(
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
        except sqlite3.OperationalError:
            return []

    def buscar_estudiante(self, cedula: str) -> tuple:
        """
        Buscar un estudiante en la tabla 'estudiantes'

        Args:
            cedula (str): Cedula del estudiante
        """
        try:
            with sqlite3.connect(self.RUTA_ABSOLUTA) as conexion:
                cursor = conexion.execute(
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
            with sqlite3.connect(self.RUTA_ABSOLUTA) as conexion:
                cursor = conexion.execute(
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
            with sqlite3.connect(self.RUTA_ABSOLUTA) as conexion:
                cursor = conexion.execute(
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
            with sqlite3.connect(self.RUTA_ABSOLUTA) as conexion:
                conexion.execute(
                    """
                delete from estudiantes where cedula = ?
                """,
                    (cedula,),
                )
        except sqlite3.OperationalError:
            return []

    def estudiantes_masculino(self) -> list:
        """
        Cantidad de estudiantes masculino

        Return:
            (list): cantidad de estudiantes masculino
        """
        try:
            with sqlite3.connect(self.RUTA_ABSOLUTA) as conexion:
                cursor = conexion.execute(
                    """
                select * from estudiantes where genero = 'masculino'
                """
                )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            return []

    def estudiantes_femenino(self) -> list:
        """
        Cantidad de estudiantes femenino

        Return:
            (list): cantidad de estudiantes femenino
        """
        try:
            with sqlite3.connect(self.RUTA_ABSOLUTA) as conexion:
                cursor = conexion.execute(
                    """
                select * from estudiantes where genero = 'femenino'
                """
                )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            return []

    def estudiantes_reprobados(self) -> list:
        """
        Cantidad de estudiantes reprobados

        Return:
            (list): cantidad de estudiantes reprobados
        """
        try:
            with sqlite3.connect(self.RUTA_ABSOLUTA) as conexion:
                cursor = conexion.execute(
                    """
                select * from estudiantes where nota < 5
                """
                )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            return []

    def estudiantes_aprobados(self) -> list:
        """
        Cantidad de estudiantes aprobados

        Return:
            (list): cantidad de estudiantes aprobados
        """
        try:
            with sqlite3.connect(self.RUTA_ABSOLUTA) as conexion:
                cursor = conexion.execute(
                    """
                select * from estudiantes where nota >= 5
                """
                )

            return cursor.fetchall()
        except sqlite3.OperationalError:
            return []
