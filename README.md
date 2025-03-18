# Ejecutor de Scripts SQL en Múltiples Bases de Datos PostgreSQL

Este proyecto es un script en Python que permite ejecutar scripts SQL de forma interactiva en varias bases de datos de un servidor PostgreSQL. Incorpora medidas de seguridad mediante autenticación basada en hash SHA-256, y cuenta con una interfaz amigable que utiliza arte ASCII y mensajes coloreados.

## Características

- **Autenticación Segura:** Solicita al usuario una clave y la valida comparando su hash SHA-256 con un hash almacenado.
- **Selección Interactiva de Bases de Datos:** Permite listar y seleccionar las bases de datos en las que se ejecutará el script SQL, ya sea seleccionando índices o eligiendo todas.
- **Ejecución de Scripts SQL:** Soporta la ejecución de múltiples consultas SQL ingresadas por el usuario, separadas por punto y coma.
- **Mensajes Visualmente Atractivos:** Utiliza la librería Colorama para imprimir mensajes de estado con colores.
- **Arte ASCII:** Muestra un encabezado con arte ASCII al iniciar la ejecución del script.

## Requisitos

- **Python 3.x**
- **PostgreSQL** (Acceso a un servidor PostgreSQL)
- **Librerías de Python:**
  - [psycopg2](https://www.psycopg.org/)
  - [colorama](https://pypi.org/project/colorama/)

## Instalación

1. **Clonar el repositorio o descargar el script:**

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Instalar las dependencias:**

   Utiliza `pip` para instalar las librerías necesarias:

   ```bash
   pip install psycopg2 colorama
   ```

## Configuración

Antes de ejecutar el script, asegúrate de configurar las siguientes variables dentro del código:

- **Credenciales del Servidor PostgreSQL:**
  - `DB_HOST`: Dirección IP o nombre del host del servidor.
  - `DB_PORT`: Puerto del servidor (por defecto, 5432).
  - `DB_USER`: Usuario con permisos para acceder a las bases de datos.
  - `DB_PASSWORD`: Contraseña del usuario.

- **Consulta de Bases de Datos:**
  - `GET_DATABASES_QUERY`: Consulta SQL para listar las bases de datos a las que se les aplicará el script. Puedes modificarla para excluir o incluir bases de datos según tus necesidades.

- **Clave de Acceso:**
  - En la función `check_password`, reemplaza `"aqui_tu_hash"` por el hash SHA-256 de la clave que desees utilizar. Puedes generar el hash con herramientas en línea o mediante un pequeño script en Python.

## Uso

1. **Ejecutar el Script:**

   Ejecuta el script desde la terminal:

   ```bash
   python __init__.py
   ```

2. **Autenticación:**
   - Se solicitará ingresar la clave de acceso de manera oculta.
   - Si la clave es correcta, se mostrará el arte ASCII y se continuará con la ejecución.

3. **Selección de Bases de Datos:**
   - El script mostrará una lista de bases de datos disponibles.
   - Podrás seleccionar las bases de datos ingresando los números correspondientes (separados por comas) o escribir `all` para seleccionar todas.

4. **Ingreso y Ejecución del Script SQL:**
   - Ingresa el script SQL que deseas ejecutar (puede incluir múltiples consultas separadas por punto y coma).
   - Confirma la ejecución cuando se te solicite.

## Consideraciones de Seguridad

- **Validación de Clave:** La clave se valida mediante la comparación de su hash SHA-256, evitando almacenar contraseñas en texto plano.
- **Acceso al Servidor:** Asegúrate de restringir el acceso a las credenciales del servidor PostgreSQL y de ejecutar el script en entornos seguros.
- **Modificación del Hash:** No olvides actualizar el valor de `stored_hash` en la función `check_password` para utilizar tu clave real.

## Créditos

- **Creado por:** JLuuu.java  
- **Última actualización:** 2025-03-18  
- **Linkedin:** [linkedin.com/in/juan-luis-mendoza-romero](https://www.linkedin.com/in/juan-luis-mendoza-romero-27bb0b221/)

## Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE) (o la licencia que prefieras).

