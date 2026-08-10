
from repository.database.connection import MySQLConnection

class ScoreRepository:
    def __init__(self):
        self.db_connection = MySQLConnection()

    def save_score(self, usurname, score, level_reached):
        conn = self.db_connection.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO historial_partidas (username, score, level_reached) VALUES (%s, %s, %s)"
                cursor.execute(query, (usurname, score, level_reached))
                conn.commit()
                print(f"Puntaje {score} de {usurname} guardado con éxito. Nivel {level_reached}.")
            except Exception as e:
                print(f"Error al guardar puntaje: {e}")

    def get_high_scores(self, limit=10):
        conn = self.db_connection.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT username, MAX(score) as max_score FROM historial_partidas GROUP BY username ORDER BY max_score DESC LIMIT %s"
                cursor.execute(query, (limit,))
                return cursor.fetchall()
            except Exception as e:
                print(f"Error al obtener puntajes altos: {e}")
        return []
