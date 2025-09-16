class Discussion:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def post_message(self, message_id, user_id, course_id, content):
        self.cursor.execute(
            "INSERT INTO discussions (message_id, user_id, course_id, content) VALUES (%s, %s, %s, %s)",
            (message_id, user_id, course_id, content)
        )
        self.conn.commit()
        print(f"✅ Message posted successfully for course {course_id}!")

    def view_messages(self, course_id):
        if course_id:
            self.cursor.execute("SELECT * FROM discussions WHERE course_id=%s", (course_id,))
        else:
            self.cursor.execute("SELECT * FROM discussions")
        for row in self.cursor.fetchall():
            print(row)

    def update_message(self, message_id, content):
        self.cursor.execute(
            "UPDATE discussions SET content=%s WHERE message_id=%s",
            (content, message_id)
        )
        self.conn.commit()
        print(f"✅ Message {message_id} updated successfully!")

    def delete_message(self, message_id):
        self.cursor.execute(
            "DELETE FROM discussions WHERE message_id=%s",
            (message_id,)
        )
        self.conn.commit()
        print(f"✅ Message {message_id} deleted successfully!")

    # Context manager support
    def close(self):
        self.cursor.close()
        self.conn.close()
        print("🔒 Database connection closed")

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
