# -*- coding: utf-8 -*-
"""Porcentaje de estudiante
Autor: Hugo Zorrilla
Descripcion: Vista de colegio
"""

import os
from rich.console import Console
from rich.table import Table

from app.Controllers.EstudianteController import EstudianteController


def visualizar_estadisticas_de_estudiantes() -> None:
    """
    Visualiza la estadistica de estudiantes del colegio
    """

    # Limpieza de la consola
    os.system("clear")

    estudiante = EstudianteController()

    # Suma total de todos los de estudiantes del colegio
    total_estudiantes: int = estudiante.cantidad_estudiantes()

    if total_estudiantes > 0:
        # Lista de estudiantes masculinos
        estudiantes_masculino: int = len(estudiante.estudiantes_masculino())

        # Lista de estudiantes femeninos
        estudiantes_femenino: int = len(estudiante.estudiantes_femenino())

        # Porcentaje de estudiantes masculinos
        porcentaje_em: float = round(estudiante.porcentaje_estudiantes_masculinos(), 2)

        # Porcentaje de estudiantes femeninos
        porcentaje_ef: float = round(estudiante.porcentaje_estudiantes_femeninos(), 2)

        # Porcentaje total de estudiantes en el colegio
        porcentaje_total_estudiantes: float = estudiante.porcentaje_total_estudiantes()

        # Objeto para imprimir tabla
        console = Console()

        # Salto de linea
        print("\n")

        # Objeto para la creacion de la tabla
        table = Table(title="Tabla de informacion")
        table.add_column("Cantidad estudiantes")
        table.add_column("Cantidad estudiantes masculino")
        table.add_column("Cantidad estudiantes femenino")
        table.add_column("Porcentaje de estudiantes masculinos")
        table.add_column("Porcentaje de estudiantes femeninos")
        table.add_column("Porcentaje total de estudiantes")

        table.add_row(
            str(total_estudiantes),
            str(estudiantes_masculino),
            str(estudiantes_femenino),
            str(porcentaje_em),
            str(porcentaje_ef),
            str(porcentaje_total_estudiantes),
        )

        console.print(table)
    else:
        print("** no hay estudiantes registrados **\n".upper())


def menu_colegio() -> int:
    """
    Menu principal del estudiante

    Returns:
        int: opcion seleccionada
    """
    opcion = 0
    while opcion not in (1, 2):
        try:
            # Limpieza de la consola
            os.system("clear")
            print(
                "** MENU COLEGIO **",
                "1. Visualizar estadisticas de estudiantes",
                "2. Salir",
                sep="\n",
            )
            opcion = int(input("ingrese una opcion: "))

            if opcion not in (1, 2):
                print("\nPor favor, ingrese una opcion valida.")
                input("Presione enter para continuar...")
                os.system("clear")
        except ValueError:
            print("\nPor favor, ingrese una opcion valida.")
            input("Presione enter para continuar...")
            os.system("clear")
    return opcion


def main() -> None:
    """
    Funcion principal del programa de la vista de colegio
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        match menu_colegio():
            # Menu principal
            case 1:
                # Visualizar datos
                visualizar_estadisticas_de_estudiantes()
                input("Presione enter para continuar...")
            case 2:
                # Salir
                break


if __name__ == "__main__":
    main()
