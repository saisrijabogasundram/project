class Enrollment:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def enroll_student(self, enrollment_id, user_id, course_id):
        self.cursor.execute(
            "INSERT INTO enrollments (enrollment_id, user_id, course_id) VALUES (%s, %s, %s)",
            (enrollment_id, user_id, course_id)
        )
        self.conn.commit()
        print(f"✅ Student {user_id} enrolled in course {course_id} successfully!")

    def view_enrollments(self):
        self.cursor.execute("SELECT * FROM enrollments")
        for row in self.cursor.fetchall():
            print(row)

    def update_enrollment(self, enrollment_id, user_id, course_id):
        if enrollment_id:
            self.cursor.execute("SELECT * FROM enrollments WHERE enrollment_id=%s", (enrollment_id,))
            if not self.cursor.fetchone():
                print(f"⚠️ Enrollment {enrollment_id} does not exist.")
            return self.cursor.fetchone()
        if user_id:
            self.cursor.execute(
                "UPDATE enrollments SET user_id=%s WHERE enrollment_id=%s", (user_id, enrollment_id))
        if course_id:
            self.cursor.execute(
                "UPDATE enrollments SET course_id=%s WHERE enrollment_id=%s", (course_id, enrollment_id))
        self.conn.commit()
        print(f"✅ Enrollment {enrollment_id} updated successfully!")
        

    def delete_enrollment(self, enrollment_id):
        self.cursor.execute("DELETE FROM enrollments WHERE enrollment_id=%s", (enrollment_id,))
        self.conn.commit()
        print(f"✅ Enrollment {enrollment_id} deleted successfully!")

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
