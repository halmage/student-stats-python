# -*- coding: utf-8 -*-
"""Porcentaje de estudiante
Autor: Hugo Zorrilla
Descripcion: Cuerpo principal del programa
"""

# Importacion de librerias
import os

# Importacion de vistas
from app.Controllers.EstudianteController import EstudianteController
from app.Views.estudiante_view import main as menu_estudiante
from app.Views.colegio_view import main as menu_colegio


# Limpieza de la consola
os.system("clear")


def menu() -> int:
    """Menu de opciones del sistema

    Returns:
        int: opcion seleccionada
    """
    opcion = 0
    while opcion not in (1, 2, 3, 4):
        try:
            # Limpieza de la consola
            os.system("clear")
            print(
                "** SISTEMA DE CONTROL ESCOLAR **",
                "1. Modulo de estudiantes",
                "2. Modulo de estadisticas colegial",
                "3. Crear base de datos",
                "4. Salir",
                sep="\n",
            )
            opcion = int(input("ingrese una opcion: "))

            if opcion not in (1, 2, 3, 4):
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
    Funcion principal del programa
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        # Menu principal
        match menu():
            case 1:
                # Menu de estudiantes
                menu_estudiante()
            case 2:
                # Menu de colegio
                menu_colegio()
            case 3:
                # Crear base de datos
                estudiante = EstudianteController()
                estado_database = estudiante.crear_tabla_estudiantes()
                print(f"\n** {estado_database} **\n")
                input("Presione enter para continuar...")
            case 4:
                # Salir
                print("\n** Gracias por usar el sistema **\n")
                input("Presione enter para continuar...")
                os.system("clear")
                break


if __name__ == "__main__":
    main()
