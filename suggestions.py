class suggestion:
    def __init__(self,cursor,conn):
        self.cursor = cursor
        self.conn = conn
    def submit_suggestion(self, suggestion_id, user_id, content):
        self.cursor.execute("INSERT INTO suggestions (suggestion_id, user_id, content) VALUES (%s, %s, %s)",
                       (suggestion_id, user_id, content))
        self.conn.commit()
        print(f"Suggestion {suggestion_id} submitted successfully!")
    def view_suggestions(self):
        self.cursor.execute("SELECT * FROM suggestions")
        for row in self.cursor.fetchall():
            print(row)
    def close(self):
        self.cursor.close()
        self.conn.close()