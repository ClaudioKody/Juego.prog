from  repository . database . connection  import  MySQLConnection

class UserRepository:
    def __init__(self):
        self.db_connection = MySQLConnection ()

    def obtener_o_crear_usuario (self, username):
        """
        Busca al usuario en la base de datos.
        Si existe, devuelve su nivel actual y puntaje máximo.
        Si no existe, lo crea de forma segura con nivel 1 y max_score O.
        
        """
        conn = self.db_connection.get_connection()
        if  not  conn : 
             print ( "Error: No hay conexión a la base  de datos." ) 
             return  1 ,  0 

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT current_level, max_score FROM usuarios WHERE username = %s", (username,))
            row = cursor.fetchone ()

            if row:
                level, max_score = row
                print (f"Usuario '{username}' encontrado. Nivel actual: {level}")

                