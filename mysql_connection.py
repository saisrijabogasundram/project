import mysql.connector
from mysql.connector import Error

print("🟢 Starting MySQL connection test...")

try:
    # Attempt to connect to MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LMS",
        port=3306  # optional, default is 3306
    )

    if connection.is_connected():
        print("✅ Connected to MySQL server successfully!")
        db_Info = connection.get_server_info()
        print(f"MySQL Server version: {db_Info}")

        # List all databases
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES;")
        databases = cursor.fetchall()
        print("📌 Databases on server:")
        for db in databases:
            print(f" - {db[0]}")

except Error as e:
    print("❌ Error while connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("🔒 MySQL connection closed.")
