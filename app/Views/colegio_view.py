# -*- coding: utf-8 -*-
"""
MÓDULO: colegio_view.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN: Maneja la interfaz de usuario para la gestión del colegio,
             incluyendo la visualización de estadísticas y el menú principal.
"""

import os
from rich.console import Console
from rich.table import Table

from app.Controllers.estadistica_controller import EstadisticaController


def visualizar_estadisticas_de_estudiantes() -> None:
    """
    Visualiza la estadistica de estudiantes del colegio
    """

    # Limpieza de la consola
    os.system("clear")

    estudiante = EstadisticaController()

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
        table = Table(title="📊 TABLA DE INFORMACION")
        table.add_column("Cantidad estudiantes", justify="center", style="cyan")
        table.add_column(
            "Cantidad estudiantes masculino", justify="center", style="magenta"
        )
        table.add_column(
            "Cantidad estudiantes femenino", justify="center", style="green"
        )
        table.add_column(
            "Porcentaje de estudiantes masculinos", justify="center", style="yellow"
        )
        table.add_column(
            "Porcentaje de estudiantes femeninos", justify="center", style="blue"
        )
        table.add_column(
            "Porcentaje total de estudiantes", justify="center", style="red"
        )

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
