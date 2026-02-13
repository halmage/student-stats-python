# -*- coding: utf-8 -*-
"""Porcentaje de estudiante
Autor: Hugo Zorrilla
Descripcion: Cuerpo principal del programa
"""

# Importacion de librerias
import os

# Importacion de vistas
from app.Controllers.estudiante_controller import EstudianteController
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
                "3. Gestion de base de datos",
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


def menu_gestion_base_de_datos() -> int:
    """Menu de opciones del sistema

    Returns:
        int: opcion seleccionada
    """
    opcion = 0
    while opcion not in (1, 2, 3):
        try:
            # Limpieza de la consola
            os.system("clear")
            print(
                "** GESTION DE BASE DE DATOS **",
                "1. Crear base de datos",
                "2. Eliminar base de datos",
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


def crear_base_de_datos() -> None:
    """
    Crea la base de datos
    """
    estudiante = EstudianteController()
    estado_database = estudiante.crear_tabla_estudiantes()
    print(f"\n** {estado_database} **\n")
    input("Presione enter para continuar...")


def eliminar_base_de_datos() -> None:
    """
    Elimina la base de datos
    """
    estudiante = EstudianteController()
    estudiante.eliminar_tabla_estudiantes()
    print("\n** Tabla eliminada exitosamente **\n")
    input("Presione enter para continuar...")


def gestion_base_de_datos() -> None:
    """
    Operaciones de la base de datos
    """
    while True:
        match menu_gestion_base_de_datos():
            case 1:
                # Limpieza de la consola
                os.system("clear")
                print("** CREAR BASE DE DATOS **")
                print(crear_base_de_datos())
            case 2:
                # Limpieza de la consola
                os.system("clear")
                print("** ELIMINAR BASE DE DATOS **\n")
                confirmacion = input(
                    "¿Estas seguro de eliminar la base de datos? (s/n): "
                )
                if confirmacion == "s":
                    print(eliminar_base_de_datos())
                else:
                    # Limpieza de la consola
                    os.system("clear")
                    print("** Operacion cancelada **\n")
                    input("Presione enter para continuar...")
            case 3:
                break


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
                # Gestion de base de datos
                gestion_base_de_datos()
            case 4:
                # Salir
                # Limpieza de la consola
                os.system("clear")
                print("** Gracias por usar el sistema **\n")
                input("Presione enter para continuar...")
                os.system("clear")
                break


if __name__ == "__main__":
    main()
