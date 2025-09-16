class Lesson:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def add_lesson(self, lesson_id, course_id, title, context):
        self.cursor.execute(
            "INSERT INTO lessons (lesson_id, course_id, title, content) VALUES (%s, %s, %s, %s)",
            (lesson_id, course_id, title, context)
        )
        self.conn.commit()
        print(f"✅ Lesson '{title}' added to course {course_id} successfully!")

    def view_lessons(self):
        self.cursor.execute("SELECT * FROM lessons")
        for row in self.cursor.fetchall():
            print(row)

    def update_lesson(self, lesson_id, course_id, title, context):
        if lesson_id:
            self.cursor.execute("SELECT * FROM lessons WHERE lesson_id=%s", (lesson_id,))
            lesson = self.cursor.fetchone()
            if not lesson:
                print(f"❌ Lesson {lesson_id} not found!")
                return

        if course_id:
            self.cursor.execute("SELECT * FROM courses WHERE course_id=%s", (course_id,))
            course = self.cursor.fetchone()
            if not course:
                print(f"❌ Course {course_id} not found!")
                return
        if title:
           self.cursor.execute("UPDATE lessons SET title=%s WHERE lesson_id=%s", (title, lesson_id))
        if context:
            self.cursor.execute("UPDATE lessons SET context=%s WHERE lesson_id=%s", (context, lesson_id))
        self.conn.commit()
        print(f"✅ Lesson {lesson_id} updated successfully!")

    def delete_lesson(self, lesson_id):
        self.cursor.execute("DELETE FROM lessons WHERE lesson_id=%s", (lesson_id,))
        self.conn.commit()
        print(f"✅ Lesson {lesson_id} deleted successfully!")

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
