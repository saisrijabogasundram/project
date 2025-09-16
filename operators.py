class User:
    def __init__(self,user_id,name,email,password,role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        
    def register(self):
        self.cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
                       (self.name, self.email, self.password, self.role))
        self.conn.commit()
        print(f"{self.role.capitalize()} registered successfully!")

    @staticmethod
    def login(self,email, password):
        self.cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = self.cursor.fetchone()
        if user:
            print(f"Welcome {user[1]} ({user[4]})")
            return user
        else:
            print("Invalid credentials")
            return None
#student class inheriting User class    
class Student(User):
    def browse_courses(self):
        self.cursor.execute("SELECT * FROM courses")
        for row in self.cursor.fetchall():
            print(row)

    def enroll_course(self, course_id):
        self.cursor.execute("INSERT INTO enrollments (user_id, course_id) VALUES (%s, %s)", (self.user_id, course_id))
        self.conn.commit()
        print(f"Enrolled in course {course_id} successfully!")
#instructor class inheriting User class
class Instructor(User):        
    def create_course(self, title, description, price):
        self.cursor.execute("INSERT INTO courses (title, description, price, instructor_id) VALUES (%s, %s, %s, %s)",
                       (title, description, price, self.user_id))
        self.conn.commit()
        print(f"Course '{title}' created successfully!")
        
    def get_id(self):
        self.cursor.execute("SELECT user_id FROM users WHERE email=%s AND password=%s", (self.email, self.password))
        return self.cursor.fetchone()[0]

    def add_lesson(self, course_id, title, content):
        self.cursor.execute("INSERT INTO lessons (course_id, title, content) VALUES (%s, %s, %s)",
                       (course_id, title, content))
        self.conn.commit()
        print(f"Lesson '{title}' added to course {course_id}")
        
    def view_enrollments(self, course_id):
        self.cursor.execute("SELECT u.name, u.email FROM enrollments e JOIN users u ON e.user_id = u.user_id WHERE e.course_id=%s", (course_id,))
        for row in self.cursor.fetchall():
            print(row)
    
class Admin(User):
    def view_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        for row in self.cursor.fetchall():
            print(row)
    
    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
        self.conn.commit()
        print(f"User {user_id} deleted successfully!")
class UserOperations:
    def __init__(self,cursor,conn):
        self.cursor = cursor
        self.conn = conn
    def register(self, name, email, password, role):
        self.cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
                       (name, email, password, role))
        self.conn.commit()
        print(f"{role.capitalize()} registered successfully!")
    def login(self, email, password):
        self.cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = self.cursor.fetchone()
        if user:
            print(f"Welcome {user[1]} ({user[4]})")
            return user
        else:
            print("Invalid credentials")
            return None
    def close(self):
        self.cursor.close()
        self.conn.close()



