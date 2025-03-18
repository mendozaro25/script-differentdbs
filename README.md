# 🔹 Ejecutor de Scripts SQL en Múltiples Bases de Datos PostgreSQL

Este proyecto es un script en Python diseñado para ejecutar consultas SQL de manera interactiva en múltiples bases de datos dentro de un servidor PostgreSQL. Implementa medidas de seguridad mediante autenticación basada en hash SHA-256 y ofrece una interfaz optimizada con arte ASCII y mensajes coloreados para mejorar la experiencia del usuario.

---

## 🚀 Características

✅ **Autenticación Segura:** Protege el acceso al sistema mediante una clave cuya validación se realiza con SHA-256.  
✅ **Selección Interactiva de Bases de Datos:** Permite elegir en qué bases de datos ejecutar los scripts, ya sea seleccionándolas individualmente o todas a la vez.  
✅ **Ejecución de Scripts SQL:** Soporta la ejecución de múltiples consultas SQL separadas por punto y coma.  
✅ **Mensajes Visuales Mejorados:** Utiliza la librería `colorama` para mostrar mensajes con colores intuitivos.  
✅ **Interfaz Estética:** Muestra un encabezado con arte ASCII para mejorar la experiencia visual.  

---

## 📌 Requisitos

🔹 **Python 3.x**  
🔹 **PostgreSQL** (Acceso a un servidor PostgreSQL)  
🔹 **Librerías Necesarias:**
   - [`psycopg2`](https://www.psycopg.org/) (para la conexión con PostgreSQL)
   - [`colorama`](https://pypi.org/project/colorama/) (para mejorar la visualización de mensajes)  

---

## ⚙️ Instalación

1️⃣ **Clona el repositorio o descarga el script:**
   ```bash
   git clone https://github.com/mendozaro25/script-differentdbs
   cd script-differentdbs
   ```

2️⃣ **Instala las dependencias:**
   ```bash
   pip install requirements.txt
   ```

---

## 🛠️ Configuración

Antes de ejecutar el script, asegúrate de configurar las siguientes variables dentro del código:

🔹 **Credenciales de Conexión:**
   - `DB_HOST`: Dirección IP o nombre del servidor PostgreSQL.
   - `DB_PORT`: Puerto de conexión (por defecto, 5432).
   - `DB_USER`: Usuario con permisos adecuados.
   - `DB_PASSWORD`: Contraseña del usuario.

🔹 **Consulta de Bases de Datos:**
   - `GET_DATABASES_QUERY`: Define cómo listar las bases de datos a utilizar, permitiendo excluir ciertas bases si es necesario.

🔹 **Clave de Acceso:**
   - En la función `check_password`, reemplaza `"aqui_tu_hash"` por el hash SHA-256 de la clave de acceso.
   - Puedes generar el hash con la siguiente línea en Python:
     ```python
     import hashlib
     print(hashlib.sha256("tu_clave_secreta".encode()).hexdigest())
     ```

---

## ▶️ Uso del Script

1️⃣ **Ejecutar el Script:**
   ```bash
   python __init__.py
   ```

2️⃣ **Autenticación:**
   - Se solicitará una clave de acceso de manera oculta.
   - Si la clave es correcta, se mostrará el arte ASCII y se continuará la ejecución.

3️⃣ **Selección de Bases de Datos:**
   - Se mostrará una lista de bases de datos disponibles.
   - Ingresa los números correspondientes (separados por comas) o escribe `all` para seleccionar todas.

4️⃣ **Ingreso y Ejecución del Script SQL:**
   - Ingresa el código SQL que deseas ejecutar.
   - Confirma antes de proceder con la ejecución.

---

## 🔐 Consideraciones de Seguridad

🔸 **Clave Protegida:** Se valida mediante hash SHA-256, evitando almacenamiento en texto plano.  
🔸 **Restricción de Accesos:** Mantén seguras las credenciales del servidor PostgreSQL.  
🔸 **Modificación del Hash:** Personaliza `stored_hash` en `check_password` para utilizar una clave segura.  

---

## 📌 Créditos

👨‍💻 **Desarrollado por:** JLuuu.java  
📅 **Última actualización:** 2025-03-18  
🔗 **LinkedIn:** [linkedin.com/in/juan-luis-mendoza-romero](https://www.linkedin.com/in/juan-luis-mendoza-romero-27bb0b221/)  

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE).  

---

