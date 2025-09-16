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

def main_menu():
    print("\n=== LMS MAIN MENU ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    return input("Enter choice: ")

def register_user():
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    role = input("Role (student/instructor/admin): ").lower()
    user = User(conn, None, name, email, password, role)
    user.register()

def login_user():
    email = input("Email: ")
    password = input("Password: ")
    user_data = User.login(conn, email, password)
    if user_data:
        role = user_data[4]
        user_id = user_data[0]
        if role == 'student':
            student_menu(user_id)
        elif role == 'instructor':
            instructor_menu(user_id)
        elif role == 'admin':
            admin_menu(user_id)

def student_menu(user_id):
    student = Student(conn, user_id, "", "", "", "student")
    prog = progress(cursor, conn)
    disc = Discussion(cursor, conn)
    notif = Notification(cursor, conn)
    feed = feedback(cursor, conn)
    cert = Certificate(cursor, conn)
    pay = Payment(cursor, conn)
    plan = upgradePlan(cursor, conn)
    support_obj = support(cursor, conn)
    
    while True:
        print("\n--- STUDENT MENU ---")
        print("1. Browse Courses")
        print("2. Enroll in Course")
        print("3. View Progress")
        print("4. View Discussions")
        print("5. Post Feedback")
        print("6. View Notifications")
        print("7. View Certificates")
        print("8. Payments")
        print("9. Upgrade Plan")
        print("10. Submit Support Ticket")
        print("11. Logout")
        choice = input("Enter choice: ")
        
        if choice == '1':
            Course(cursor, conn).view_courses()
        elif choice == '2':
            course_id = input("Enter Course ID to enroll: ")
            student.enroll_course(course_id)
        elif choice == '3':
            prog.view_progress()
        elif choice == '4':
            course_id = input("Enter Course ID to view discussions: ")
            disc.view_messages(course_id)
        elif choice == '5':
            feed_id = input("Feedback ID: ")
            course_id = input("Course ID: ")
            rating = int(input("Rating (1-5): "))
            comments = input("Comments: ")
            feed.submit_feedback(feed_id, user_id, course_id, rating, comments)
        elif choice == '6':
            notif.view_notifications(user_id)
        elif choice == '7':
            cert.view_certificates(user_id)
        elif choice == '8':
            action = input("1. Make Payment  2. View Payments: ")
            if action == '1':
                pay_id = input("Payment ID: ")
                course_id = input("Course ID: ")
                amount = float(input("Amount: "))
                pay.process_payment(pay_id, user_id, course_id, amount, "completed")
            elif action == '2':
                pay.view_payments(user_id)
        elif choice == '9':
            new_plan = input("Enter new plan: ")
            plan.upgrade_plan(user_id, new_plan)
        elif choice == '10':
            ticket_id = input("Ticket ID: ")
            subject = input("Subject: ")
            description = input("Description: ")
            support_obj.submit_ticket(ticket_id, user_id, subject, description)
        elif choice == '11':
            break
        else:
            print("Invalid choice!")


def instructor_menu(user_id):
    instructor = Instructor(conn, user_id, "", "", "", "instructor")
    course_obj = Course(cursor, conn)
    lesson_obj = Lesson(cursor, conn)
    disc = Discussion(cursor, conn)
    notif = Notification(cursor, conn)
    feed = feedback(cursor, conn)
    cert = Certificate(cursor, conn)
    
    while True:
        print("\n--- INSTRUCTOR MENU ---")
        print("1. Create Course")
        print("2. Add Lesson")
        print("3. View Enrollments")
        print("4. View Discussions")
        print("5. View Feedback")
        print("6. Issue Certificates")
        print("7. Logout")
        choice = input("Enter choice: ")
        
        if choice == '1':
            course_id = input("Course ID: ")
            course_name = input("Course Name: ")
            description = input("Description: ")
            course_obj.create_course(course_id, course_name, description, user_id)
        elif choice == '2':
            course_id = input("Course ID: ")
            lesson_id = input("Lesson ID: ")
            title = input("Lesson Title: ")
            content = input("Content: ")
            lesson_obj.add_lesson(lesson_id, course_id, title, content)
        elif choice == '3':
            course_id = input("Course ID: ")
            instructor.view_enrollments(course_id)
        elif choice == '4':
            course_id = input("Course ID: ")
            disc.view_messages(course_id)
        elif choice == '5':
            feed.view_feedback()
        elif choice == '6':
            cert_id = input("Certificate ID: ")
            course_id = input("Course ID: ")
            cert.issue_certificate(cert_id, user_id, course_id)
        elif choice == '7':
            break
        else:
            print("Invalid choice!")


def admin_menu(user_id):
    admin = Admin(conn, user_id, "", "", "", "admin")
    report_obj = Report(cursor, conn)
    analytics_obj = Analytics(cursor, conn)
    course_obj = Course(cursor, conn)
    user_ops = UserOperations(conn)
    
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. View All Users")
        print("2. Delete User")
        print("3. User Activity Report")
        print("4. Course Popularity Report")
        print("5. Analytics")
        print("6. Manage Courses")
        print("7. Logout")
        choice = input("Enter choice: ")
        
        if choice == '1':
            admin.view_all_users()
        elif choice == '2':
            uid = input("Enter User ID to delete: ")
            admin.delete_user(uid)
        elif choice == '3':
            report_obj.user_activity_report()
        elif choice == '4':
            report_obj.course_popularity_report()
        elif choice == '5':
            analytics_obj.user_growth()
            analytics_obj.course_completion_rates()
        elif choice == '6':
            sub_choice = input("1. Create 2. Update 3. Delete: ")
            if sub_choice == '1':
                cid = input("Course ID: ")
                cname = input("Name: ")
                desc = input("Description: ")
                instructor_id = input("Instructor ID: ")
                course_obj.create_course(cid, cname, desc, instructor_id)
            elif sub_choice == '2':
                cid = input("Course ID to update: ")
                cname = input("New Name: ")
                desc = input("New Description: ")
                instructor_id = input("Instructor ID: ")
                course_obj.update_course(cid, cname, desc, instructor_id)
            elif sub_choice == '3':
                cid = input("Course ID to delete: ")
                course_obj.delete_course(cid)
        elif choice == '7':
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting LMS...")
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice!")
