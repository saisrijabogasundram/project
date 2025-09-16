class Progress:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def track_progress(self, progress_id, student_id, course_id, lesson_id, status):
        self.cursor.execute(
            "INSERT INTO progress (progress_id, user_id, course_id, lesson_id, status) VALUES (%s, %s, %s, %s, %s)",
            (progress_id, student_id, course_id, lesson_id, status)
        )
        self.conn.commit()
        print(f"✅ Progress for student {student_id} in course {course_id} tracked successfully!")

    def view_progress(self):
        self.cursor.execute("SELECT * FROM progress")
        for row in self.cursor.fetchall():
            print(row)
        return

    def update_progress(self, progress_id, status, lesson_id, course_id, student_id):
        if progress_id:
            self.cursor.execute("SELECT * FROM progress WHERE progress_id=%s", (progress_id,))
            if not self.cursor.fetchone():
                print(f"⚠️ Progress ID {progress_id} not found.")
                return
        if status:
            self.cursor.execute("UPDATE progress SET status=%s WHERE progress_id=%s", (status, progress_id))
            self.conn.commit()
            print(f"✅ Progress {progress_id} status updated to '{status}' successfully!")
            return
        if lesson_id:
            self.cursor.execute("UPDATE progress SET lesson_id=%s WHERE progress_id=%s", (lesson_id, progress_id))
            self.conn.commit()
            print(f"✅ Progress {progress_id} lesson updated to '{lesson_id}' successfully!")
            return
        if course_id:
            self.cursor.execute("UPDATE progress SET course_id=%s WHERE progress_id=%s", (course_id, progress_id))
            self.conn.commit()
            print(f"✅ Progress {progress_id} course updated to '{course_id}' successfully!")
            return
        if student_id:
            self.cursor.execute("UPDATE progress SET user_id=%s WHERE progress_id=%s", (student_id, progress_id))
            self.conn.commit()
            print(f"✅ Progress {progress_id} student updated to '{student_id}' successfully!")
            return
        self.conn.commit()
        print(f"✅ Progress {progress_id} updated successfully!")

    def delete_progress(self, progress_id):
        self.cursor.execute("DELETE FROM progress WHERE progress_id=%s", (progress_id,))
        self.conn.commit()
        print(f"✅ Progress {progress_id} deleted successfully!")

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
