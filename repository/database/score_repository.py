from repository.database.connection import MySQLConnection

class ScoreRepository:
    def __init__(self):
        self.db_connection = MySQLConnection ()

    def save_score(self, player_name, score):
        conn = self.db_connection.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO scores (player_name, score) VALUES(%s, %s)"
                cursor.execute (query, (player_name, score))
                conn.commit()
                print (f"Puntaje {score} de {player_name} guardado con éxito.")
            except Exception as e:
                print (f"Error al guardar puntaje: {e}")

    
    

