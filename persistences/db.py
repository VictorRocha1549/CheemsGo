import os
import mysql.connector

def obtener_conexion():
    try:
        # Leemos los valores desde el entorno
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER', 'avnadmin')
        db_pw = os.environ.get('DB_PW')
        db_port = os.environ.get('DB_PORT', '10667')
        db_name = os.environ.get('DB_NAME', 'defaultdb')

        # Conexión a la base de datos
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pw,
            database=db_name,
            port=db_port
        )
        return conn
        
    except Exception as ex:
        print(f"Error en la conexión a la base de datos: {ex}")
        # En Python, nulo se escribe None
        return None