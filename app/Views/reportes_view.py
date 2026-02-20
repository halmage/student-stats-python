"""
MÓDULO: reportes_view.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN: Maneja la interfaz de usuario para la generación de reportes
             estadísticos y la exportación de datos.
"""

import os

from app.Controllers.reporte_controller import ReporteController
from app.Controllers.estudiante_controller import EstudianteController

# Importacion de validaciones
from app.package.validaciones import Validaciones


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
        print(
            "** MENU CURSOS **",
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
            print(f"{validar_curso}\n")
            input("Presione enter para continuar...")
            os.system("clear")
        else:
            break
    return curso


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
            print(
                "** REPORTES DEL COLEGIO **",
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
                print("\nPor favor, ingrese una opcion valida.")
                input("Presione enter para continuar...")
                os.system("clear")
        except ValueError:
            print("\nPor favor, ingrese una opcion valida.")
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
                print(f"\n** {mensaje} **\n")
                input("Presione enter para continuar...")
            case 2:
                mensaje = reporte.reporte_estudiantes_aprobados_reprobados()
                print(f"\n** {mensaje} **\n")
                input("Presione enter para continuar...")
            case 3:
                mensaje = reporte.reporte_estudiantes_aprobados()
                print(f"\n** {mensaje} **\n")
                input("Presione enter para continuar...")
            case 4:
                mensaje = reporte.reporte_estudiantes_reprobados()
                print(f"\n** {mensaje} **\n")
                input("Presione enter para continuar...")
            case 5:
                # Limpieza de la consola
                while True:
                    os.system("clear")
                    curso = menu_curso()
                    mensaje = reporte.reporte_estudiantes_por_curso(curso)
                    print(f"\n** {mensaje} **")
                    continuar = Validaciones().continuar_operacion()
                    if not continuar:
                        break
            case 6:
                break
