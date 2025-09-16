from flask import Flask, request, jsonify
from db import conn, cursor
from user import User, Student, Instructor, Admin, UserOperations
from course import Course
from lesson import Lesson
from enrollment import Enrollment
from progress import progress
from discussion import Discussion
from notification import Notification
from feedback import feedback
from certificate import Certificate
from analytics import Analytics
from payment import Payment
from upgradePlan import upgradePlan
from support import support
from report import Report

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    user = User(conn, None, data['name'], data['email'], data['password'], data['role'])
    user.register()
    return jsonify({"message": f"{data['role']} registered successfully!"})

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user_data = User.login(conn, data['email'], data['password'])
    if user_data:
        return jsonify({"user": user_data})
    else:
        return jsonify({"error": "Invalid credentials"}), 401 

@app.route('/courses', methods=['GET'])
def get_courses():
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    return jsonify({"courses": courses})

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    course_obj = Course(cursor, conn)
    course_obj.create_course(data['course_id'], data['course_name'], data['description'], data['instructor_id'])
    return jsonify({"message": "Course created successfully!"})

@app.route('/lessons', methods=['POST'])
def add_lesson():
    data = request.json
    lesson_obj = Lesson(cursor, conn)
    lesson_obj.add_lesson(data['lesson_id'], data['course_id'], data['title'], data['content'])
    return jsonify({"message": "Lesson added successfully!"})

@app.route('/enroll', methods=['POST'])
def enroll_student():
    data = request.json
    enroll_obj = Enrollment(cursor, conn)
    enroll_obj.enroll_student(data['enrollment_id'], data['user_id'], data['course_id'])
    return jsonify({"message": "Student enrolled successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
