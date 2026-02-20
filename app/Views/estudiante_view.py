"""
MÓDULO: estudiante_view.py
PROYECTO: Sistema de Gestión Estadística Estudiantil
AUTOR: Hugo Zorrilla
DESCRIPCIÓN: Maneja la interfaz de usuario para el registro y consulta
de estudiantes.
"""

# Importacion de librerias
import os
from rich.console import Console
from rich.table import Table

# Importacion de controladores
from app.Controllers.estudiante_controller import EstudianteController
from app.Controllers.estadistica_controller import EstadisticaController

# Importacion de validaciones
from app.package.validaciones import Validaciones


def registro_de_datos() -> dict | None:
    """
    Ingreso de datos por el usuario

    Return:
        (dict): toma registro de los datos del usuario ingresado
    """
    estudiante = EstudianteController()

    continuar: bool = True
    while continuar:
        # Limpieza de la consola
        os.system("clear")
        print("** registro datos del estudiante **".upper())

        cedula: str = ""  # Ingreso de la cedula del estudiante
        validar_cedula: str = ""  # Validacion de la cedula
        while True:
            # Validando si el cedula es un numero positivo
            cedula = input("\nIngrese cedula: ")
            validar_cedula = estudiante.validar_cedula(cedula)

            if validar_cedula or estudiante.buscar_estudiante(cedula):
                # Muestra error si la cedula no es un numero positivo de 8 digitos

                if validar_cedula is None:
                    print("\nError: La cedula ya existe")
                    continuar = Validaciones().continuar_operacion()
                    if not continuar:
                        break
                else:
                    print(f"\n{validar_cedula}")
            else:
                break
        if not continuar:
            # Si no se desea continuar
            break

        # Ingreso nombre del estudiante
        nombre: str = ""
        validar_nombre: str = ""
        while True:
            # Validando si el nombre es un caracter
            nombre = input("\nIngrese nombre: ").strip()
            validar_nombre = estudiante.validar_nombre(nombre)

            if validar_nombre:
                print(f"\n{validar_nombre}")
            else:
                break

        # Ingreso edad del estudiante
        edad: int = ""
        validar_edad: str = ""
        while True:
            # Validando si el edad es un numero positivo o esta entre 10 y 17 años
            edad = input("\nIngrese edad: ")
            validar_edad = estudiante.validar_edad(edad)

            if validar_edad:
                # Muestra error si la edad no es un numero positivo o esta entre 10 y 17 años
                print(f"\n{validar_edad}")
                continuar = Validaciones().continuar_operacion()
                if not continuar:
                    break
            else:
                break
        if not continuar:
            # Si no se desea continuar
            break

        # Ingreso genero del estudiante
        genero: str = ""
        validar_genero: str = ""
        while True:
            # Validando si el genero es femenino o masculino
            genero = input("\nIngrese genero (femenino/masculino): ")
            validar_genero = estudiante.validar_genero(genero)

            if validar_genero:
                # Muestra error si el genero no es femenino o masculino
                print(f"\n{validar_genero}")
            else:
                break

        # Ingreso curso del estudiante
        curso: str = ""
        validar_curso: str = ""
        while True:
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
            validar_curso = estudiante.validar_curso(curso)

            if validar_curso:
                # Muestra error si el curso no es femenino o masculino
                print(f"\n{validar_curso}")
            else:
                break

        # Ingresa nota del estudiante
        nota: str = ""
        validar_nota: str = ""
        while True:
            # Validando si el genero es femenino o masculino
            nota = input("\nIngrese nota del estudiante (0-10): ")
            validar_nota = estudiante.validar_nota(nota)

            if validar_nota:
                # Muestra error si el genero no es femenino o masculino
                print(f"\n{validar_nota}")
            else:
                break

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

    Returns:
        None
    """
    # Muestra el estudiante
    console = Console()
    table = Table(title="📊 LISTADO DE ESTUDIANTES")
    table.add_column("Cedula", justify="right", style="cyan")
    table.add_column("Nombre", style="magenta")
    table.add_column("Edad", justify="center", style="green")
    table.add_column("Genero", justify="center", style="yellow")
    table.add_column("Curso", justify="center", style="blue")
    table.add_column("Nota", justify="center", style="red")
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

    Returns:
        None
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

    Returns:
        None
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** mostrar estudiantes **".upper())

        # Llama a la clase estudiante
        estudiantes = EstudianteController()

        # Muestra todos los estudiantes
        datos_estudiantes = estudiantes.mostrar_estudiantes()

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

    Returns:
        None
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** mostrar estudiantes masculinos **".upper())

        # Llama a la clase estudiante
        estudiantes = EstadisticaController()

        # Muestra todos los estudiantes masculinos
        datos_estudiantes = estudiantes.estudiantes_masculino()

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

    Returns:
        None
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** mostrar estudiantes femeninos **".upper())

        # Llama a la clase estudiante
        estudiantes = EstadisticaController()

        # Muestra todos los estudiantes femeninos
        datos_estudiantes = estudiantes.estudiantes_femenino()

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

    Returns:
        None
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** mostrar estudiantes aprobados **".upper())

        # Llama a la clase estudiante
        estudiantes = EstadisticaController()

        # Muestra todos los estudiantes aprobados
        datos_estudiantes = estudiantes.estudiantes_aprobados()

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

    Returns:
        None
    """
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** mostrar estudiantes reprobados **".upper())

        # Llama a la clase estudiante
        estudiantes = EstadisticaController()

        # Muestra todos los estudiantes reprobados
        datos_estudiantes = estudiantes.estudiantes_reprobados()

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


def mostrar_estudiantes_por_curso() -> None:
    """
    Muestra los estudiantes por curso
    Returns:
        None
    """
    while True:
        # Limpieza de la consola
        os.system("clear")
        # Llama a la clase estudiante
        estudiantes = EstudianteController()
        # Muestra todos los estudiantes por curso
        curso = menu_curso()
        datos_estudiantes = estudiantes.mostrar_estudiantes_por_curso(curso)
        if datos_estudiantes:
            # Limpieza de la consola
            os.system("clear")
            # Muestra todos los estudiantes por curso
            text = "Datos de los estudiantes por curso"
            tabla_informacion_estudiante(datos_estudiantes, text, False)
        else:
            print(f"\n** No se encontraron estudiantes en el curso {curso.upper()} **")
        break


def menu_mostrar_estudiantes() -> int:
    """
    Menu para mostrar estudiantes

    Returns:
        int: opcion seleccionada
    """
    # Limpieza de la consola
    os.system("clear")
    opcion = 0
    while opcion not in (1, 2, 3, 4, 5, 6, 7):
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
                "6. Mostrar estudiantes por curso",
                "7. Salir",
                sep="\n",
            )
            opcion = int(input("ingrese una opcion: "))

            if opcion not in (1, 2, 3, 4, 5, 6, 7):
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

    Returns:
        None
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
                # Mostrar estudiantes por curso
                while True:
                    mostrar_estudiantes_por_curso()
                    continuar = Validaciones().continuar_operacion()
                    if not continuar:
                        break
            case 7:
                # Salir
                break


def eliminar_estudiante() -> None:
    """
    Elimina un estudiante de la tabla 'estudiantes'

    Returns:
        None
    """
    # Ingreso de la cedula del estudiante
    cedula: str = ""
    validar_cedula = ""
    while True:
        # Limpieza de la consola
        os.system("clear")

        print("** eliminar estudiante **".upper())
        # Validando si el cedula es un numero positivo
        cedula = input("\nIngrese cedula: ")
        estudiante = EstudianteController()
        validar_cedula: str = estudiante.validar_cedula(cedula)

        if validar_cedula:
            print(f"\n{validar_cedula}")
            input("\nPresione enter para continuar...")
            continue

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
                # Limpieza de la consola
                os.system("clear")
                print("** Estudiante eliminado exitosamente **")
                input("\nPresione enter para continuar...")
                break
            # Salir de la operacion eliminar estudiante
            break
        print("\n** No se encontro el estudiante **")
        # Pregunta si desea buscar otro estudiante
        continuar = Validaciones().continuar_operacion()
        if not continuar:
            break


def menu_estudiante() -> int:
    """
    Menu principal del estudiante

    Returns:
        int: opcion seleccionada
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

    Returns:
        None
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
