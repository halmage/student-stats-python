# -*- coding: utf-8 -*-
"""Porcentaje de estudiante
Autor: Hugo Zorrilla
Descripcion: Cuerpo principal del programa
"""

# Importacion de librerias
import os

# Importacion de vistas
from app.Views.estudiante_view import main as menu_estudiante
from app.Views.colegio_view import main as menu_colegio


# Limpieza de la consola
os.system("clear")


def menu() -> int:
    """
    Menu principal del programa
    """
    opcion = 0
    while opcion not in (1, 2, 3):
        try:
            # Limpieza de la consola
            os.system("clear")
            print(
                "** SISTEMA DE CONTROL ESCOLAR **",
                "1. Modulo de estudiantes",
                "2. Modulo de estadisticas colegial",
                "3. Salir",
                sep="\n",
            )
            opcion = int(input("ingrese una opcion: "))

            if opcion not in (1, 2, 3):
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
                print("\n** Gracias por usar el sistema **")
                input("Presione enter para continuar...")
                os.system("clear")
                break


if __name__ == "__main__":
    main()
