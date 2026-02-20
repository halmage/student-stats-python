# -*- coding: utf-8 -*-
"""
Porcentaje de estudiante

MÓDULO: main.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN: Cuerpo principal del programa
"""

# Importacion de librerias
import os

# Importacion de vistas
from app.Views.reportes_view import main as menu_reportes
from app.Views.colegio_view import main as menu_colegio
from app.Views.estudiante_view import main as menu_estudiante
from app.Views.gestion_base_de_datos_view import main as menu_gestion_base_de_datos

# Limpieza de la consola
os.system("clear")


def menu() -> int:
    """Menu de opciones del sistema

    Returns:
        int: opcion seleccionada
    """
    opcion = 0
    while opcion not in (1, 2, 3, 4, 5):
        try:
            # Limpieza de la consola
            os.system("clear")
            print(
                "** SISTEMA DE CONTROL ESCOLAR **",
                "1. Modulo de estudiantes",
                "2. Modulo de estadisticas colegial",
                "3. Modulo de reportes",
                "4. Gestion de base de datos",
                "5. Salir",
                sep="\n",
            )
            opcion = int(input("ingrese una opcion: "))

            if opcion not in (1, 2, 3, 4, 5):
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
                # Menu de reportes
                menu_reportes()
            case 4:
                # Gestion de base de datos
                menu_gestion_base_de_datos()
            case 5:
                # Salir
                # Limpieza de la consola
                os.system("clear")
                print("** Gracias por usar el sistema **\n")
                input("Presione enter para continuar...")
                os.system("clear")
                break


if __name__ == "__main__":
    main()
