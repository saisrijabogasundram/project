class Notification:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def send_notification(self, notification_id, user_id, message):
        self.cursor.execute(
            "INSERT INTO notifications (notification_id, user_id, message) VALUES (%s, %s, %s)",
            (notification_id, user_id, message)
        )
        self.conn.commit()
        print(f"✅ Notification sent to user {user_id}!")

    def view_notifications(self, user_id):
        if user_id:
            self.cursor.execute("SELECT * FROM notifications WHERE user_id=%s", (user_id,))
        else:
            self.cursor.execute("SELECT * FROM notifications")
        for row in self.cursor.fetchall():
            print(row)

    def update_notification(self, notification_id, message):
        self.cursor.execute(
            "UPDATE notifications SET message=%s WHERE notification_id=%s",
            (message, notification_id)
        )
        self.conn.commit()
        print(f"✅ Notification {notification_id} updated successfully!")

    def delete_notification(self, notification_id):
        self.cursor.execute(
            "DELETE FROM notifications WHERE notification_id=%s",
            (notification_id,)
        )
        self.conn.commit()
        print(f"✅ Notification {notification_id} deleted successfully!")

    # Context manager support
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
