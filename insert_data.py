from mydb import Database
from users import User

mydb = Database("localhost", "root", "123456", "LMS", 3306)
print("✅ Database connected successfully!")

if __name__ == "__main__":
  mydb = Database("localhost", "root", "123456", "LMS", 3306)
  if mydb.conn and mydb.cursor:
        user = User(mydb, None, "Smitha", "smitha@example.com", "pass123", "student")
        user.register()

        # 3. Fetch and display all users
        User.fetch_all(mydb)

    # 4. Close database connection
mydb.close()
print("🟢 Script finished.")

