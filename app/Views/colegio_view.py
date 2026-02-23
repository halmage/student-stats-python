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
import matplotlib.pyplot as plt

from app.Controllers.estadistica_controller import EstadisticaController

# Objeto para imprimir tabla
console = Console()

estudiante = EstadisticaController()


def visualizar_tabla_de_estudiantes() -> None:
    """
    Visualiza la estadistica de estudiantes del colegio
    """

    # Limpieza de la consola
    os.system("clear")

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
        console.print("[bold red]❌ No hay estudiantes registrados[/bold red]\n")


def visualizar_grafico_de_estudiantes() -> None:
    """
    Visualiza la estadistica de estudiantes del colegio
    """

    # Limpieza de la consola
    os.system("clear")

    # Suma total de todos los de estudiantes del colegio
    total_estudiantes: int = estudiante.cantidad_estudiantes()

    if total_estudiantes > 0:
        # Lista de estudiantes masculinos
        estudiantes_masculino: int = len(estudiante.estudiantes_masculino())

        # Lista de estudiantes femeninos
        estudiantes_femenino: int = len(estudiante.estudiantes_femenino())

        # Salto de linea
        print("\n")

        # Objeto para la creacion de la tabla
        fig, ax = plt.subplots()

        generos: list[str] = ["Masculino", "Femenino"]
        counts: list[int] = [estudiantes_masculino, estudiantes_femenino]
        bar_labels: list[str] = ["Masculino", "Femenino"]
        bar_colors: list[str] = ["tab:blue", "tab:red"]

        ax.bar(generos, counts, label=bar_labels, color=bar_colors)

        ax.set_ylabel("Cantidad de estudiantes")
        ax.set_title("Cantidad de estudiantes por genero")
        ax.legend(title="Genero")

        plt.show()
    else:
        console.print("[bold red]❌ No hay estudiantes registrados[/bold red]\n")


def visualizar_grafico_de_porcentaje_de_estudiantes() -> None:
    """
    Visualiza el porcentaje de estudiantes del colegio
    """
    # Limpieza de la consola
    os.system("clear")

    # Suma total de todos los de estudiantes del colegio
    total_estudiantes: int = estudiante.cantidad_estudiantes()

    if total_estudiantes > 0:
        # Porcentaje de estudiantes masculinos
        porcentaje_em: float = round(estudiante.porcentaje_estudiantes_masculinos(), 2)

        # Porcentaje de estudiantes femeninos
        porcentaje_ef: float = round(estudiante.porcentaje_estudiantes_femeninos(), 2)

        # Salto de linea
        print("\n")

        # Objeto para la creacion de la tabla
        fig, ax = plt.subplots()

        fruits: list[str] = ["Masculino", "Femenino"]
        counts: list[int] = [porcentaje_em, porcentaje_ef]
        bar_labels: list[str] = ["Masculino", "Femenino"]
        bar_colors: list[str] = ["tab:blue", "tab:red"]

        ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

        ax.set_ylabel("Porcentaje de estudiantes")
        ax.set_title("Porcentaje de estudiantes por genero")
        ax.legend(title="Genero")

        plt.show()
    else:
        console.print("[bold red]❌ No hay estudiantes registrados[/bold red]\n")


def menu_colegio() -> int:
    """
    Menu principal del estudiante

    Returns:
        int: opcion seleccionada
    """
    opcion = 0
    while opcion not in (1, 2, 3, 4):
        try:
            # Limpieza de la consola
            os.system("clear")
            console.print(
                "📋 MENU COLEGIO",
                "1. Visualizar tabla de estudiantes",
                "2. Visualizar grafico de estudiantes",
                "3. Visualizar grafico de porcentaje de estudiantes",
                "4. Salir",
                sep="\n",
            )
            opcion = int(input("ingrese una opcion: "))

            if opcion not in (1, 2, 3, 4):
                console.print(
                    "\n[bold red]❌ Por favor, ingrese una opcion valida.[/bold red]\n"
                )
                input("Presione enter para continuar...")
                os.system("clear")
        except ValueError:
            console.print(
                "\n[bold red]❌ Por favor, ingrese una opcion valida.[/bold red]\n"
            )
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
                visualizar_tabla_de_estudiantes()
                input("Presione enter para continuar...")
            case 2:
                # Visualizar grafico
                visualizar_grafico_de_estudiantes()
                input("Presione enter para continuar...")
            case 3:
                # Visualizar porcentaje
                visualizar_grafico_de_porcentaje_de_estudiantes()
                input("Presione enter para continuar...")
            case 4:
                # Salir
                break


if __name__ == "__main__":
    main()
