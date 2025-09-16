class Certificate:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def issue_certificate(self, certificate_id, user_id, course_id):
        self.cursor.execute(
            "INSERT INTO certificates (certificate_id, user_id, course_id) VALUES (%s, %s, %s)",
            (certificate_id, user_id, course_id)
        )
        self.conn.commit()
        print(f"✅ Certificate {certificate_id} issued to user {user_id} for course {course_id}!")

    def view_certificates(self, user_id, course_id):
        query = "SELECT * FROM certificates"
        params = ()
        if user_id and course_id:
            query += " WHERE user_id=%s AND course_id=%s"
            params = (user_id, course_id)
        elif user_id:
            query += " WHERE user_id=%s"
            params = (user_id,)
        elif course_id:
            query += " WHERE course_id=%s"
            params = (course_id,)

        self.cursor.execute(query, params)
        for row in self.cursor.fetchall():
            print(row)
        return

    def delete_certificate(self, certificate_id):
        self.cursor.execute("DELETE FROM certificates WHERE certificate_id=%s", (certificate_id,))
        self.conn.commit()
        print(f"✅ Certificate {certificate_id} deleted successfully!")

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
