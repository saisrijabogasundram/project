class Feedback:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def submit_feedback(self, feedback_id, user_id, course_id, rating, comments):
        self.cursor.execute(
            "INSERT INTO feedback (feedback_id, user_id, course_id, rating, comments) VALUES (%s, %s, %s, %s, %s)",
            (feedback_id, user_id, course_id, rating, comments)
        )
        self.conn.commit()
        print(f"✅ Feedback submitted successfully by user {user_id}!")

    def view_feedback(self, course_id, user_id):
        query = "SELECT * FROM feedback"
        params = ()
        if course_id and user_id:
            query += " WHERE course_id=%s AND user_id=%s"
            params = (course_id, user_id)
        elif course_id:
            query += " WHERE course_id=%s"
            params = (course_id,)
        elif user_id:
            query += " WHERE user_id=%s"
            params = (user_id,)

        self.cursor.execute(query, params)
        for row in self.cursor.fetchall():
            print(row)
        return

    def update_feedback(self, feedback_id, rating, comments):
        if feedback_id:
            print(f"🔍 Searching for feedback ID {feedback_id}...")
        if rating:
            self.cursor.execute("SELECT * FROM feedback WHERE feedback_id=%s", (feedback_id,))
        if comments:
            self.cursor.execute("SELECT * FROM feedback WHERE comments=%s", (comments))
        if not self.cursor.fetchone():
            print(f"❌ Feedback ID {feedback_id} not found.")
            return
        self.conn.commit()
        print(f"✅ Feedback {feedback_id} updated successfully!")

    def delete_feedback(self, feedback_id):
        self.cursor.execute("DELETE FROM feedback WHERE feedback_id=%s", (feedback_id,))
        self.conn.commit()
        print(f"✅ Feedback {feedback_id} deleted successfully!")

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
