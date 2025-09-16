import mysql.connector

# Database connection class
class Database:
    def __init__(self, host, user, password, database,port):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def _enter_(self):
        return self 

    def _exit_(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


