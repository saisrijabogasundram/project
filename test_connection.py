print("Step 1: Script started")

try:
    import mysql.connector
    print("Step 2: mysql.connector imported successfully")
except Exception as e:
    print("❌ Failed to import mysql.connector:", e)

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LMS"
    )
    print("Step 3: Connected to MySQL successfully")
except Exception as e:
    print("❌ Failed to connect to MySQL:", e)
