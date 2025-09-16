class Course:
    def __init__(self,cursor,conn):
        self.cursor = cursor
        self.conn = conn

    # Create a new course
    def create_course(self, course_id, course_name, description, instructor_id):
        self.cursor.execute(
            "INSERT INTO courses (course_id, course_name, description, instructor_id) VALUES (%s, %s, %s, %s)",
            (course_id, course_name, description, instructor_id)
        )
        self.conn.commit()
        print(f"✅ Course '{course_name}' created successfully!")

    # View all courses
    def view_courses(self):
        self.cursor.execute("SELECT * FROM courses")
        courses = self.cursor.fetchall()
        for row in courses:
            print(row)
        return courses

    # Update course info (only provided fields)
    def update_course(self, course_id, course_name, description, instructor_id):
        if course_id:
            self.cursor.execute("UPDATE courses SET course_id=%s WHERE course_id=%s",
                       (course_id, course_id))
        if course_name:
           self.cursor.execute("UPDATE courses SET course_name=%s WHERE course_id=%s",
                       (course_name, course_id))
        if description:
            self.cursor.execute("UPDATE courses SET description=%s WHERE course_id=%s",
                       (description, course_id))
        if instructor_id:
            self.cursor.execute("UPDATE courses SET instructor_id=%s WHERE course_id=%s",
                       (instructor_id, course_id))
        self.conn.commit()
        print(f"✅ Course {course_id} updated successfully!")

    # Delete a course
    def delete_course(self, course_id):
        self.cursor.execute("DELETE FROM courses WHERE course_id=%s", (course_id,))
        self.conn.commit()
        print(f"✅ Course {course_id} deleted successfully!")

    # Close cursor and connection
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("🔒 Database connection closed")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __del__(self):
        self.close()