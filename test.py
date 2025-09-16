print("Step 1: Script started...")

try:
    import mysql.connector
    print("Step 2: mysql.connector imported successfully!")
except Exception as e:
    print("❌ Failed to import mysql.connector:", e)

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LMS"
    )
    print("Step 3: Connected to MySQL successfully!")
    cursor = db.cursor(dictionary=True)
except Exception as e:
    print("❌ Failed to connect to MySQL:", e)
    db = None
    cursor = None

if db and cursor:
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("Step 4: Fetched users from database:")
        for row in rows:
            print(row)
    except Exception as e:
        print("❌ Failed to fetch data:", e)
    finally:
        cursor.close()
        db.close()
        print("Step 5: Database connection closed.")

print("Step 6: Script finished.")
