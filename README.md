# Sistema de Gestión de Estadísticas Estudiantiles (Python + SQLite)

Este proyecto es una herramienta de análisis de datos escolares desarrollada en **Python** , diseñada para proporcionar métricas clave sobre el cuerpo estudiantil de una institución educativa. Utiliza **SQLite** como motor de base de datos para garantizar una gestión de la información ligera, eficiente y sin necesidad de configuraciones complejas de servidor.

### 📋 Características Principales

El programa permite procesar la información de los alumnos para obtener los siguientes indicadores de forma automatizada:

- **Reporte de Rendimiento Académico:** Filtrado y visualización detallada de la lista completa de estudiantes **aprobados** y **reprobados** .
- **Persistencia de Datos:** Integración con una base de datos local SQLite para el almacenamiento seguro y consulta rápida de los registros.

### 🚀 Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Base de Datos:** SQLite3
- **Librerías:** `sqlite3` (para la gestión de la BD) y lógica de programación estructurada para el cálculo de porcentajes.

### ⚙️ Funcionamiento General

El sistema se conecta a la base de datos `colegio.db`, extrae los registros de la tabla de estudiantes y aplica funciones de agregación para determinar las estadísticas. La lógica de aprobación se basa en los criterios de calificación estándar definidos en el código fuente.
