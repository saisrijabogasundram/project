class User:
    def __init__(self, db, user_id, name, email, password, role):
        self.db = db
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        
    def register(self):
        self.db.cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
                       (self.name, self.email, self.password, self.role))
        self.db.conn.commit()
        print(f"{self.role.capitalize()} registered successfully!")

    @staticmethod
    def login(db,email, password):
        db.cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = db.cursor.fetchone()
        if user:
            print(f"✅Welcome {user[1]} ({user[4]})")
            return user
        else:
            print("❌Invalid credentials")
            return None
            

#student class inheriting User class    
class Student(User):
    def browse_courses(self):
        self.db.cursor.execute("SELECT * FROM courses")
        for row in self.db.cursor.fetchall():
            print(row)
        return self.db.cursor.fetchall()
    def enroll_course(self, course_id):
        self.db.cursor.execute("INSERT INTO enrollments (user_id, course_id) VALUES (%s, %s)", (self.user_id, course_id))
        self.db.conn.commit()
        print(f"Enrolled in course {course_id} successfully!")
#instructor class inheriting User class
class Instructor(User):        
    def create_course(self, course_id, course_name, description, price):
        self.db.cursor.execute("INSERT INTO courses (course_id, course_name, description, price, instructor_id) VALUES (%s, %s, %s, %s, %s)",
                       (course_id, course_name, description, price, self.user_id))
        self.db.conn.commit()
        print(f"Course '{course_name}' created successfully!")

    def get_id(self):
        self.db.cursor.execute("SELECT user_id FROM users WHERE email=%s AND password=%s", (self.email, self.password))
        return self.db.cursor.fetchone()[0]

    def add_lesson(self, course_id, title, content):
        self.db.cursor.execute("INSERT INTO lessons (course_id, title, content) VALUES (%s, %s, %s)",
                       (course_id, title, content))
        self.db.conn.commit()
        print(f"Lesson '{title}' added to course {course_id}")
        
    def view_enrollments(self, course_id):
        self.db.cursor.execute("SELECT u.name, u.email FROM enrollments e JOIN users u ON e.user_id = u.user_id WHERE e.course_id=%s", (course_id,))
        for row in self.db.cursor.fetchall():
            print(row)
        return self.db.cursor.fetchall()
    
class Admin(User):
    def view_all_users(self):
        self.db.cursor.execute("SELECT * FROM users")
        for row in self.db.cursor.fetchall():
            print(row)
        return self.db.cursor.fetchall()
    
    def delete_user(self, user_id):
        self.db.cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
        self.db.conn.commit()
        print(f"User {user_id} deleted successfully!")
class UserOperations:
    def __init__(self, db):
        self.db = db
        self.conn = db.conn
        self.cursor = db.cursor
    def update_profile(self, user_id, name,email, password):
        if name:
            self.cursor.execute("UPDATE users SET name=%s WHERE user_id=%s", (name, user_id))
        if email:
            self.cursor.execute("UPDATE users SET email=%s WHERE user_id=%s", (email, user_id))
        if password:
            self.cursor.execute("UPDATE users SET password=%s WHERE user_id=%s", (password, user_id))
        self.conn.commit()
        print("✅ Profile updated successfully!")

    # Delete user
    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
        self.conn.commit()
        print(f"✅ User {user_id} deleted successfully!")
    def get_user_by_email(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        return self.cursor.fetchone()
    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
        return self.cursor.fetchone()
    def list_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
    def list_instructors(self):
        self.cursor.execute("SELECT * FROM users WHERE role='instructor'")
        return self.cursor.fetchall()
    def list_students(self):
        self.cursor.execute("SELECT * FROM users WHERE role='student'")
        return self.cursor.fetchall()
    def list_admins(self):
        self.cursor.execute("SELECT * FROM users WHERE role='admin'")
        return self.cursor.fetchall()
     # Close connection
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
  










