class Report:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def user_activity_report(self):
        self.cursor.execute("""
            SELECT u.user_id, u.name, u.email, u.role, COUNT(e.enrollment_id) AS total_enrollments
            FROM users u
            LEFT JOIN enrollments e ON u.user_id = e.user_id
            GROUP BY u.user_id, u.name, u.email, u.role
            ORDER BY total_enrollments DESC
        """)
        rows = self.cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("⚠️ No user activity found.")

    def course_popularity_report(self):
        self.cursor.execute("""
            SELECT c.course_id, c.course_name, COUNT(e.enrollment_id) AS total_enrollments
            FROM courses c
            LEFT JOIN enrollments e ON c.course_id = e.course_id
            GROUP BY c.course_id, c.course_name
            ORDER BY total_enrollments DESC
        """)
        rows = self.cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("⚠️ No course enrollment data found.")

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
