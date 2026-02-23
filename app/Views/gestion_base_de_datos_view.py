"""
MÓDULO: gestion_base_de_datos_view.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN: Interfaz de usuario (Consola/Web) para la administración del
esquema de base de datos. Permite la inicialización y mantenimiento de tablas.
"""

import os

from app.Views.colegio_view import console

# Importacion de controladores
from app.Controllers.estudiante_controller import EstudianteController


def crear_base_de_datos() -> None:
    """
    Crea la base de datos
    """
    estudiante = EstudianteController()
    estado_database = estudiante.crear_tabla_estudiantes()
    if estado_database == "Base de datos creada exitosamente":
        console.print(f"\n[bold green]{'✅'} {estado_database} [/bold green]\n")
    else:
        console.print(f"\n[bold yellow]{'⚠️'}  {estado_database} [/bold yellow]\n")
    input("Presione enter para continuar...")


def eliminar_base_de_datos() -> None:
    """
    Elimina la base de datos
    """
    estudiante = EstudianteController()
    estudiante.eliminar_tabla_estudiantes()
    console.print(
        "\n[bold green]✅ Base de datos eliminada exitosamente [/bold green]\n"
    )
    input("Presione enter para continuar...")


def menu() -> int:
    """Menu de opciones del sistema

    Returns:
        int: opcion seleccionada
    """
    opcion = 0
    while opcion not in (1, 2, 3):
        try:
            # Limpieza de la consola
            os.system("clear")
            console.print(
                "🛢  GESTION DE BASE DE DATOS",
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


def main() -> None:
    """
    Operaciones de la base de datos
    """
    while True:
        match menu():
            case 1:
                # Limpieza de la consola
                os.system("clear")
                console.print("🛢  CREAR BASE DE DATOS")
                print(crear_base_de_datos())
            case 2:
                # Limpieza de la consola
                os.system("clear")
                console.print(
                    "⚠️ [bold yellow] ELIMINARAS LA BASE DE DATOS [/bold yellow]⚠️\n"
                )
                confirmacion = input(
                    "¿Estas seguro de eliminar la base de datos 🛢? (s/n): "
                )
                if confirmacion == "s":
                    print(eliminar_base_de_datos())
                else:
                    # Limpieza de la consola
                    os.system("clear")
                    console.print("[bold red]❌ Operacion cancelada [/bold red]\n")
                    input("Presione enter para continuar...")
            case 3:
                break
