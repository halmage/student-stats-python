"""
MÓDULO: reportes_view.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN:
    Maneja la interfaz de usuario para la generación de reportes
    estadísticos y la exportación de datos.
"""

import os
from rich.console import Console


from app.Controllers.reporte_controller import ReporteController
from app.Controllers.estudiante_controller import EstudianteController

# Importacion de validaciones
from app.package.validaciones import Validaciones

console = Console()


def menu_curso() -> str:
    """Menu de opciones del sistema

    Returns:
        str: curso seleccionado
    """
    # Ingreso curso del estudiante
    curso: str = ""
    validar_curso: str = ""
    while True:
        # Validando si el genero es femenino o masculino
        console.print(
            "📋 MENU CURSOS",
            "matematicas",
            "ciencias",
            "historia",
            "geografia",
            "biologia",
            sep="\n",
        )
        curso = input("Ingrese el curso que quieres generar el reporte: ")
        validar_curso = EstudianteController().validar_curso(curso)

        if validar_curso:
            # Muestra error si el curso no es femenino o masculino
            console.print(f"\n[bold red]❌ {validar_curso}[/bold red]\n")
            input("Presione enter para continuar...")
            os.system("clear")
        else:
            break
    return curso


def aviso_estado_reporte(mensaje: str) -> None:
    """Muestra el aviso del estado del reporte"""
    if mensaje == "Reporte generado exitosamente":
        console.print(f"\n[bold green]✅ {mensaje}[/bold green]")
    else:
        console.print(f"\n[bold red]❌ {mensaje}[/bold red]")


def menu() -> int:
    """Menu de opciones del sistema

    Returns:
        int: opcion seleccionada
    """
    opcion = 0
    while opcion not in (1, 2, 3, 4, 5, 6):
        try:
            # Limpieza de la consola
            os.system("clear")
            console.print(
                "📋 REPORTES DEL COLEGIO",
                "1. Reporte general de estudiantes",
                "2. Reporte de estudiantes aprobados y reprobados",
                "3. Reporte de estudiantes aprobados",
                "4. Reporte de estudiantes reprobados",
                "5. Reporte de estudiantes por curso",
                "6. Salir",
                sep="\n",
            )
            opcion = int(input("ingrese una opcion: "))

            if opcion not in (1, 2, 3, 4, 5, 6):
                console.print(
                    "[bold red]❌ Por favor, ingrese una opcion valida.[/bold red]"
                )
                input("Presione enter para continuar...")
                os.system("clear")
        except ValueError:
            console.print(
                "[bold red]❌ Por favor, ingrese una opcion valida.[/bold red]"
            )
            input("Presione enter para continuar...")
            os.system("clear")
    return opcion


def main():
    """Menu principal del sistema"""
    reporte = ReporteController()
    while True:
        opcion = menu()
        match opcion:
            case 1:
                mensaje = reporte.reporte_listado_estudiantes()
                aviso_estado_reporte(mensaje)
                input("\nPresione enter para continuar...")
            case 2:
                mensaje = reporte.reporte_estudiantes_aprobados_reprobados()
                aviso_estado_reporte(mensaje)
                input("\nPresione enter para continuar...")
            case 3:
                mensaje = reporte.reporte_estudiantes_aprobados()
                aviso_estado_reporte(mensaje)
                input("\nPresione enter para continuar...")
            case 4:
                mensaje = reporte.reporte_estudiantes_reprobados()
                aviso_estado_reporte(mensaje)
                input("\nPresione enter para continuar...")
            case 5:
                # Limpieza de la consola
                while True:
                    os.system("clear")
                    curso = menu_curso()
                    mensaje = reporte.reporte_estudiantes_por_curso(curso)
                    aviso_estado_reporte(mensaje)
                    continuar = Validaciones().continuar_operacion()
                    if not continuar:
                        break
            case 6:
                break
