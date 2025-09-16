class Analytics:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def user_growth(self):
        self.cursor.execute("""
            SELECT DATE(created_at) AS signup_date, COUNT(user_id) AS total_signups
            FROM users
            GROUP BY signup_date
            ORDER BY signup_date
        """)
        for row in self.cursor.fetchall():
            print(f"📅 Date: {row[0]}, Total Signups: {row[1]}")

    def course_completion_rates(self):
        self.cursor.execute("""
            SELECT c.course_id, c.title,
                   COUNT(e.enrollment_id) AS total_enrollments,
                   SUM(CASE WHEN e.completed = 1 THEN 1 ELSE 0 END) AS total_completions,
                   (SUM(CASE WHEN e.completed = 1 THEN 1 ELSE 0 END) / COUNT(e.enrollment_id)) * 100 AS completion_rate
            FROM courses c
            LEFT JOIN enrollments e ON c.course_id = e.course_id
            GROUP BY c.course_id, c.title
        """)
        for row in self.cursor.fetchall():
            print(f"📘 Course: {row[1]} (ID: {row[0]}), Enrollments: {row[2]}, Completions: {row[3]}, Completion Rate: {row[4]:.2f}%")

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
