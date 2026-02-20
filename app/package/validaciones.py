"""
Clase Validaciones

MÓDULO: validaciones.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN: Contiene la clase Validaciones, responsable de manejar
la lógica de confirmación de operaciones y validación de entradas del usuario.
"""


class Validaciones:
    """Clase que representa las validaciones"""

    def continuar_operacion(self) -> bool:
        """
        Verifica si el usuario desea continuar con la operacion

        Return:
            (bool): True si el usuario desea continuar, False si no
        """
        continuar = ""
        while continuar not in ["si", "no", "s", "n"]:
            continuar = input("\n¿Desea continuar? (si/no): ").lower().strip()

            if continuar not in ["si", "no", "s", "n"]:
                print("\nError: el dato tiene que ser si o no")

        if continuar in ("si", "s"):
            # Si el usuario desea continuar
            return True

        # Si el usuario no desea continuar
        return False

    def continuar_eliminar(self) -> bool:
        """
        Verifica si el usuario desea eliminar el estudiante

        Return:
            (bool): True si el usuario desea eliminar, False si no
        """
        continuar = ""
        while continuar not in ["si", "no", "s", "n"]:
            continuar = (
                input("\n¿Desea eliminar el estudiante? (si/no): ").lower().strip()
            )

            if continuar not in ["si", "no", "s", "n"]:
                print("\nError: el dato tiene que ser si o no")

        if continuar in ("si", "s"):
            # Si el usuario desea eliminar
            return True

        # Si el usuario no desea eliminar
        return False
