"""estudiante
Autor: Hugo Zorrilla
Fecha: 20/01/2026
Descripcion: Vista del estudiante
"""

# Importacion de librerias
import os
from rich.console import Console
from rich.table import Table

# Importacion de controladores
from app.Controllers.EstudianteController import EstudianteController

# Importacion de validaciones
from app.package.Validaciones import Validaciones


def registro_de_datos() -> None:
    """
    Ingreso de datos por el usuario

    Return:
        (dict): toma registro de los datos del usuario ingresado
    """
    continuar: bool = True
    while continuar:
        # Limpieza de la consola
        os.system("clear")
        print("** registro datos del estudiante **".upper())

        cedula: str = ""  # Ingreso de la cedula del estudiante
        existe_estudiante: bool = False  # Existe estudiante
        while (
            not cedula.isdigit()
            or int(cedula) < 0
            or len(cedula) != 8
            or existe_estudiante
        ):
            # Validando si el cedula es un numero positivo
            cedula = input("\nIngrese cedula: ")

            # Comprueba si el estudiante existe
            estudiante = EstudianteController()
            existe_estudiante: bool = estudiante.buscar_estudiante(cedula)

            if not cedula.isdigit() or int(cedula) < 0 or len(cedula) != 8:
                # Muestra error si la cedula no es un numero positivo de 8 digitos
                print("\nError: el dato tiene que ser un numero positivo de 8 digitos")

            if existe_estudiante:
                # Muestra error si el estudiante ya existe
                print("\nError: el estudiante ya existe")
                continuar = Validaciones().continuar_operacion()
                if not continuar:
                    break
        if not continuar:
            # Si no se desea continuar
            break

        # Ingreso nombre del estudiante
        nombre: str = ""
        while not nombre.isalpha():
            # Validando si el nombre es un caracter
            nombre = input("\nIngrese nombre: ")

            if not nombre:
                print("\nError: el dato tiene que ser caracter")

        # Ingreso edad del estudiante
        edad: int = ""
        while not edad.isdigit() or int(edad) not in range(10, 18):
            # Validando si el edad es un numero positivo o esta entre 10 y 17 años
            edad = input("\nIngrese edad: ")

            if not edad.isdigit() or int(edad) < 0:
                print("\nError: el dato tiene que ser un numero positivo")
            if int(edad) not in range(10, 18):
                print("\nError: el estudiante tiene que tener entre 10 y 17 años")
                continuar = Validaciones().continuar_operacion()
                if not continuar:
                    break
        if not continuar:
            # Si no se desea continuar
            break

        # Ingreso genero del estudiante
        genero: str = ""
        while genero not in ["femenino", "masculino"]:
            # Validando si el genero es femenino o masculino
            genero = input("\nIngrese genero (femenino/masculino): ")

            if genero not in ["femenino", "masculino"]:
                print("\nError: el dato tiene que ser femenino o masculino")

        # Ingreso curso del estudiante
        curso: str = ""
        while not curso.isalpha() or curso not in [
            "matematicas",
            "ciencias",
            "historia",
            "geografia",
            "biologia",
        ]:
            # Validando si el genero es femenino o masculino
            print(
                "\nCursos del colegio:",
                "matematicas",
                "ciencias",
                "historia",
                "geografia",
                "biologia",
                sep="\n",
            )
            curso = input("Ingrese el curso que esta el estudiante: ")

            if not curso.isalpha() or curso not in [
                "matematicas",
                "ciencias",
                "historia",
                "geografia",
                "biologia",
            ]:
                print("\nError: el dato no es caracter o no es un curso del colegio")

        # Ingresa nota del estudiante
        nota: str = ""
        while not nota.isdigit() or float(nota) < 0 or float(nota) > 10:
            # Validando si el genero es femenino o masculino
            nota = input("\nIngrese nota del estudiante (0-10): ")

            if not nota.isdigit() or float(nota) < 0 or float(nota) > 10:
                print("\nError: el dato tiene que ser un numero positivo entre 0 y 10")

        keywords = {
            "cedula": int(cedula),
            "nombre": nombre,
            "edad": int(edad),
            "genero": genero,
            "curso": curso,
            "nota": float(nota),
        }

        estudiante = EstudianteController(**keywords)
        estudiante.crear_estudiante()

        print("\n** Estudiante creado exitosamente **")

        continuar = Validaciones().continuar_operacion()
        if not continuar:
            break


def tabla_informacion_estudiante(
    datos: dict | list, text: str, rango_busqueda: bool
) -> None:
    """
    Tabla de informacion del estudiante

    Args:
        datos (dict | list): Datos del estudiante
        text (str): Texto que se muestra en la tabla
        rango_busqueda (bool): Indica si se muestra un solo estudiante (True) o todos (False)
    """
    # Muestra el estudiante
    console = Console()
    table = Table(title=text, show_lines=True)
    table.add_column("Cedula", justify="center")
    table.add_column("Nombre", justify="center")
    table.add_column("Edad", justify="center")
    table.add_column("Genero", justify="center")
    table.add_column("Curso", justify="center")
    table.add_column("Nota", justify="center")
    if rango_busqueda:
        # mostrar informacion de un solo estudiante (diccionario)
        table.add_row(
            str(datos["cedula"]),
            datos["nombre"],
            str(datos["edad"]),
            datos["genero"],
            datos["curso"],
            str(datos["nota"]),
        )
    else:
        # Mostrar informacion de todos los estudiantes (lista)
        for dato in datos:
            table.add_row(
                str(dato["cedula"]),
                dato["nombre"],
                str(dato["edad"]),
                dato["genero"],
                dato["curso"],
                str(dato["nota"]),
            )
    console.print(table)


def mostrar_estudiante() -> None:
    """
    Mostrar estudiantes
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** buscar estudiante **".upper())

        # Ingreso de la cedula del estudiante
        cedula: str = ""
        while not cedula.isdigit() or int(cedula) < 0 or len(cedula) not in [8]:
            # Validando si el cedula es un numero positivo
            cedula = input("\nIngrese cedula: ")

            if not cedula.isdigit() or int(cedula) < 0 or len(cedula) not in [8]:
                print("\nError: el dato tiene que ser un numero positivo de 8 digitos")

            # Llama a la clase estudiante
            estudiante = EstudianteController()

            # Muestra el estudiante en caso de que exista
            datos_estudiante = estudiante.mostrar_estudiante(cedula)

            if datos_estudiante:
                # Limpieza de la consola
                os.system("clear")
                text = "Datos del estudiante"
                tabla_informacion_estudiante(datos_estudiante, text, True)

            else:
                print("\n** No se encontro el estudiante **")

        # Pregunta si desea buscar otro estudiante
        continuar = Validaciones().continuar_operacion()
        if not continuar:
            break


def mostrar_estudiantes() -> None:
    """
    Mostrar todos los estudiantes de la tabla 'estudiantes'
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** mostrar estudiantes **".upper())

        # Llama a la clase estudiante
        estudiante = EstudianteController()

        # Muestra todos los estudiantes
        datos_estudiantes = estudiante.mostrar_estudiantes()

        if datos_estudiantes:
            # Limpieza de la consola
            os.system("clear")
            # Muestra todos los estudiantes
            text = "Datos de los estudiantes"
            tabla_informacion_estudiante(datos_estudiantes, text, False)
        else:
            print("\n** No se encontraron estudiantes **")

        input("\nPresione enter para continuar...")
        break


def mostrar_estudiantes_masculino() -> None:
    """
    Muestra todos los estudiantes masculinos
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** mostrar estudiantes masculinos **".upper())

        # Llama a la clase estudiante
        estudiante = EstudianteController()

        # Muestra todos los estudiantes masculinos
        datos_estudiantes = estudiante.estudiantes_masculino()

        if datos_estudiantes:
            # Limpieza de la consola
            os.system("clear")
            # Muestra todos los estudiantes masculinos
            text = "Datos de los estudiantes masculinos"
            tabla_informacion_estudiante(datos_estudiantes, text, False)
        else:
            print("\n** No se encontraron estudiantes masculinos **")

        input("\nPresione enter para continuar...")
        break


def mostrar_estudiantes_femenino() -> None:
    """
    Muestra todos los estudiantes femeninos
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** mostrar estudiantes femeninos **".upper())

        # Llama a la clase estudiante
        estudiante = EstudianteController()

        # Muestra todos los estudiantes femeninos
        datos_estudiantes = estudiante.estudiantes_femenino()

        if datos_estudiantes:
            # Limpieza de la consola
            os.system("clear")
            # Muestra todos los estudiantes femeninos
            text = "Datos de los estudiantes femeninos"
            tabla_informacion_estudiante(datos_estudiantes, text, False)
        else:
            print("\n** No se encontraron estudiantes femeninos **")

        input("\nPresione enter para continuar...")
        break


def mostrar_estudiantes_aprobados() -> None:
    """
    Muestra los estudiantes aprobados
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** mostrar estudiantes aprobados **".upper())

        # Llama a la clase estudiante
        estudiante = EstudianteController()

        # Muestra todos los estudiantes aprobados
        datos_estudiantes = estudiante.estudiantes_aprobados()

        if datos_estudiantes:
            # Limpieza de la consola
            os.system("clear")
            # Muestra todos los estudiantes aprobados
            text = "Datos de los estudiantes aprobados"
            tabla_informacion_estudiante(datos_estudiantes, text, False)
        else:
            print("\n** No se encontraron estudiantes aprobados **")

        input("\nPresione enter para continuar...")
        break


def mostrar_estudiantes_reprobados() -> None:
    """
    Muestra los estudiantes reprobados
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** mostrar estudiantes reprobados **".upper())

        # Llama a la clase estudiante
        estudiante = EstudianteController()

        # Muestra todos los estudiantes reprobados
        datos_estudiantes = estudiante.estudiantes_reprobados()

        if datos_estudiantes:
            # Limpieza de la consola
            os.system("clear")
            # Muestra todos los estudiantes reprobados
            text = "Datos de los estudiantes reprobados"
            tabla_informacion_estudiante(datos_estudiantes, text, False)
        else:
            print("\n** No se encontraron estudiantes reprobados **")

        input("\nPresione enter para continuar...")
        break


def eliminar_estudiante() -> None:
    """
    Elimina un estudiante de la tabla 'estudiantes'
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** eliminar estudiante **".upper())

        # Ingreso de la cedula del estudiante
        cedula: str = ""
        while not cedula.isdigit() or int(cedula) < 0 or len(cedula) not in [8]:
            # Validando si el cedula es un numero positivo
            cedula = input("\nIngrese cedula: ")

            if not cedula.isdigit() or int(cedula) < 0 or len(cedula) not in [8]:
                print("\nError: el dato tiene que ser un numero positivo de 8 digitos")

            # Llama a la clase estudiante
            estudiante = EstudianteController()

            # Muestra el estudiante en caso de que exista
            datos_estudiante = estudiante.mostrar_estudiante(cedula)

            if datos_estudiante:
                # Limpieza de la consola
                os.system("clear")
                # Muestra el estudiante
                text = "Datos del estudiante"
                tabla_informacion_estudiante(datos_estudiante, text, True)

                print("\n** Aviso: Se eliminara el estudiante **")
                # Pregunta si desea eliminar el estudiante
                continuar = Validaciones().continuar_eliminar()
                if continuar:
                    # Elimina el estudiante en caso de que exista
                    estudiante.eliminar_estudiante(cedula)

                    print("\n** Estudiante eliminado exitosamente **")
            else:
                print("\n** No se encontro el estudiante **")

        # Pregunta si desea eliminar otro estudiante
        continuar = Validaciones().continuar_operacion()
        if not continuar:
            break


def menu_mostrar_estudiantes() -> int:
    """
    Menu para mostrar estudiantes
    """
    # Limpieza de la consola
    os.system("clear")
    opcion = 0
    while opcion not in (1, 2, 3, 4, 5, 6):
        try:
            # Limpieza de la consola
            os.system("clear")
            print(
                "** MENU MOSTRAR ESTUDIANTES **",
                "1. Mostrar todos los estudiantes",
                "2. Mostrar estudiantes masculinos",
                "3. Mostrar estudiantes femeninos",
                "4. Mostrar estudiantes aprobados",
                "5. Mostrar estudiantes reprobados",
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


def mostrar_datos_estudiantes() -> None:
    """
    Muestra los datos de los estudiantes
    """
    while True:
        # Limpieza de la consola
        os.system("clear")
        match menu_mostrar_estudiantes():
            case 1:
                # Mostrar todos los estudiantes
                mostrar_estudiantes()
            case 2:
                # Mostrar estudiantes masculinos
                mostrar_estudiantes_masculino()
            case 3:
                # Mostrar estudiantes femeninos
                mostrar_estudiantes_femenino()
            case 4:
                # Mostrar estudiantes aprobados
                mostrar_estudiantes_aprobados()
            case 5:
                # Mostrar estudiantes reprobados
                mostrar_estudiantes_reprobados()
            case 6:
                # Salir
                break


def menu_estudiante() -> int:
    """
    Menu principal del estudiante
    """
    opcion = 0
    while opcion not in (1, 2, 3, 4, 5):
        try:
            # Limpieza de la consola
            os.system("clear")
            print(
                "** MENU ESTUDIANTE **",
                "1. Ingresar datos del estudiante",
                "2. Visualizar datos del estudiante",
                "3. Mostrar datos de los estudiantes",
                "4. Eliminar estudiante",
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
    Funcion principal del programa de la vista del estudiante
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        match menu_estudiante():
            # Menu principal
            case 1:
                # Registro de datos
                registro_de_datos()
            case 2:
                # Visualizar datos
                mostrar_estudiante()
            case 3:
                # Mostrar todos los estudiantes
                mostrar_datos_estudiantes()
            case 4:
                # Eliminar estudiante
                eliminar_estudiante()
            case 5:
                # Salir
                break


if __name__ == "__main__":
    main()
