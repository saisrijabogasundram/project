import mysql.connector
from mysql.connector import Error

print("🟢 Starting MySQL connection test...")

try:
    print("Attempting to connect to MySQL...")
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="LMS",
        port=3306
    )
    print("Connection object created:", connection)

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

except mysql.connector.InterfaceError as ie:
    print("❌ InterfaceError:", ie)
except mysql.connector.DatabaseError as de:
    print("❌ DatabaseError:", de)
except mysql.connector.ProgrammingError as pe:
    print("❌ ProgrammingError:", pe)
except mysql.connector.Error as e:
    print("❌ MySQL Error:", e)
except Exception as ex:
    print("❌ Other Exception:", ex)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("🔒 MySQL connection closed.")
    else:
        print("⚠ No active connection to close.")

print("🟢 Script finished.")
