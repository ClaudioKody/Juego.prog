import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from patterns.singleton.database_connection import DatabaseConnection

load_dotenv()

class MySQLConnection(DatabaseConnection):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MySQLConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def __init__(self):
        super().__init__()
        if not self.connection or not self.connection.is_connected():
            self._conectar()

    def _conectar(self):
        try:
            host = os.getenv("DB_HOST", "localhost")
            user = os.getenv("DB_USER", "root")
            port = int(os.getenv("DB_PORT", "3307"))
            password = os.getenv("DB_PASSWORD", "")
            database = os.getenv("DB_NAME", "juego_programacion2")
<<<<<<< HEAD
            
=======
            port = int(os.getenv("DB_PORT", 3306))

>>>>>>> 09740fbf089694e161534f17a284f03182452729
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                port=port,
                password=password,
                database=database,
                port=port,
                connection_timeout=5,
                use_pure=True
            )
            if self.connection.is_connected():
                print("Conexión a MySQL establecida con éxito mediante .env.")
        except Error as err:
            print(f"Error al conectar a MySQL: {err}")
            self.connection = None

    def get_connection(self):
        try:
            if self.connection and self.connection.is_connected():
                return self.connection
            else:
                self._conectar()
                return self.connection
        except Error:
            self._conectar()
            return self.connection

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a MySQL cerrada.")
            self.connection = None