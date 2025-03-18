import psycopg2
from colorama import Fore, Style, init
import getpass
import hashlib

init(autoreset=True)

# Configuración del servidor PostgreSQL
DB_HOST = "192.168.XX.XXX"  # Cambia esto si tu servidor está en otro host
DB_PORT = "5432"            # Puerto por defecto de PostgreSQL
DB_USER = "postgres"        # Usuario con permisos para acceder a todas las bases de datos
DB_PASSWORD = "XXXX"        

# Consulta para obtener todas las bases de datos
GET_DATABASES_QUERY = """
SELECT datname
FROM pg_database
WHERE datistemplate = false AND datname NOT IN ('postgres', 'otras_bases_de_datos_a_excluir');
"""

# Arte ASCII para el encabezado
ASCII_ART = r"""
                   
           ___      |\________/)
          [_,_])    \ /       \|
         /|=T=|]     /   __  __\
         |\ " //     |_  9   p ]\
         ||'-'/--.  / /\ =|  \|\ \
        /|| <\/> |\ | '._, @ @)<_)
       | |\   |  |   \.__/(_;_)
       |  .   H  |   |  :  '='|
       |  |  _H__/  _| :      |
        \  '.__  \ /  ;      ';
       __'-._(_}==.'  :       ;
      (___|    /-' |   :.     :
     [.-'  \   |   \   \ ;   :
    .-'     |  |    |  |   ":
   /        |==|     \  \  /  \_
  /         [  |      '._\_ -._ \
 /           \__)   __.- \ \   )\\
/       |        /.'      >>)
|        \       |\     |
|     .'  '-.    | \    /
|    /     /     / /   /
           |    /
     /     |   /
    /      |  /
   /       | /
  /        |/   creado por: JLuuu.java
 /         /    ultima actualizacion: 2025-03-18
|         /     ig: @juanmendoza_25
|        |
"""

def check_password():
    """
    Solicita la clave al usuario y la valida comparando el hash de la entrada
    con el hash almacenado.
    """
    stored_hash = "aqui_tu_hash"
    
    # Solicitar la clave sin mostrarla en pantalla
    password = getpass.getpass("Ingrese la clave: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    if password_hash == stored_hash:
        return True
    else:
        print(Fore.RED + "Clave incorrecta. Saliendo del programa." + Style.RESET_ALL)
        return False

def get_user_input():
    """
    Solicita al usuario que ingrese el script SQL a ejecutar.
    Retorna el script ingresado como una cadena.
    """
    print("\nPor favor, ingrese el script SQL a ejecutar en las bases de datos.")
    print("Puede incluir múltiples consultas separadas por punto y coma (;).")
    print("Presione Enter dos veces para finalizar la entrada:\n")
    
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    
    return "\n".join(lines)

def select_databases(databases):
    """
    Permite al usuario seleccionar de la lista de bases de datos en las que se ejecutará el script.
    El usuario puede elegir por número (puede ingresar varios separados por comas) o 'all' para seleccionar todas.
    """
    print("\nBases de datos detectadas:")
    for i, db in enumerate(databases, start=1):
        print(f"{i}. {db}")
    
    print("\nIngrese el número o los números (separados por coma) de las bases de datos en las que desea ejecutar el script.")
    print("O escriba 'all' para seleccionar todas las bases de datos.")
    seleccion = input("Selección: ").strip()
    
    if seleccion.lower() == "all":
        return databases
    else:
        indices = []
        for item in seleccion.split(","):
            item = item.strip()
            if item.isdigit():
                idx = int(item)
                if 1 <= idx <= len(databases):
                    indices.append(idx - 1)
                else:
                    print(Fore.RED + f"Índice {idx} fuera de rango." + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Entrada inválida: {item}" + Style.RESET_ALL)
        if not indices:
            print(Fore.RED + "No se seleccionó ninguna base de datos válida. Se ejecutará en todas las bases de datos." + Style.RESET_ALL)
            return databases
        return [databases[i] for i in indices]

def execute_on_all_databases(sql_script, databases):
    """
    Ejecuta el script SQL proporcionado en las bases de datos seleccionadas del servidor PostgreSQL.
    """
    try:
        # Conexión al servidor PostgreSQL (sin especificar una base de datos)
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.autocommit = True  # Necesario para ejecutar consultas como CREATE DATABASE
        cursor = conn.cursor()

        # Iterar sobre cada base de datos seleccionada
        for db_name in databases:
            print(f"\nProcesando base de datos: {db_name}")
            try:
                # Conectar a la base de datos específica
                db_conn = psycopg2.connect(
                    host=DB_HOST,
                    port=DB_PORT,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    database=db_name
                )
                db_cursor = db_conn.cursor()

                # Ejecutar el script SQL en la base de datos
                db_cursor.execute(sql_script)
                db_conn.commit()
                print(Fore.GREEN + f"Script ejecutado correctamente en {db_name}" + Style.RESET_ALL)

                # Cerrar la conexión a la base de datos
                db_cursor.close()
                db_conn.close()
            except Exception as e:
                print(Fore.RED + f"Error al procesar la base de datos {db_name}: {e}" + Style.RESET_ALL)

        # Cerrar la conexión al servidor principal
        cursor.close()
        conn.close()

    except Exception as e:
        print(Fore.RED + f"Error al conectar al servidor PostgreSQL: {e}" + Style.RESET_ALL)

def main():
    # Verificar clave de acceso antes de continuar
    if not check_password():
        return

    # Mostrar el arte ASCII
    print(ASCII_ART)
    
    # Obtener la lista de bases de datos
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Obtener la lista de bases de datos
        cursor.execute(GET_DATABASES_QUERY)
        databases = [row[0] for row in cursor.fetchall()]

        # Cerrar la conexión
        cursor.close()
        conn.close()
    except Exception as e:
        print(Fore.RED + f"Error al obtener la lista de bases de datos: {e}" + Style.RESET_ALL)
        return

    # Permitir al usuario seleccionar las bases de datos donde se ejecutará el script
    selected_databases = select_databases(databases)
    
    # Mostrar las bases de datos seleccionadas
    print("\nBases de datos seleccionadas:")
    for db in selected_databases:
        print(f"- {db}")

    # Solicitar al usuario que ingrese el script SQL
    sql_script = get_user_input()
    
    # Verificar si el usuario ingresó algo
    if not sql_script.strip():
        print("No se ingresó ningún script SQL. Saliendo del programa.")
        return
    
    # Confirmación antes de ejecutar
    print("---------------------------------------------------------------------")
    print("\nScript SQL a ejecutar:\n")
    print(sql_script)
    confirm = input("\n¿Desea continuar? (s/n): ").strip().lower()
    
    if confirm != 's':
        print("Operación cancelada por el usuario.")
        return
    
    # Ejecutar el script en las bases de datos seleccionadas
    print("\nIniciando la ejecución del script en las bases de datos seleccionadas...")
    execute_on_all_databases(sql_script, selected_databases)
    print("\nEjecución completada.")

if __name__ == "__main__":
    main()
