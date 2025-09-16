class Payment:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def process_payment(self, payment_id, user_id, course_id, amount, status="completed"):
        self.cursor.execute(
            "INSERT INTO payments (payment_id, user_id, course_id, amount, status) VALUES (%s, %s, %s, %s, %s)",
            (payment_id, user_id, course_id, amount, status)
        )
        self.conn.commit()
        print(f"💰 Payment {payment_id} processed successfully for User {user_id} (Amount: {amount})")

    def view_payments(self, user_id):
        self.cursor.execute("SELECT * FROM payments WHERE user_id=%s", (user_id,))
        for row in self.cursor.fetchall():
            print(f"Payment ID: {row[0]}, Course ID: {row[2]}, Amount: {row[3]}, Status: {row[4]}")

    def refund_payment(self, payment_id):
        self.cursor.execute("UPDATE payments SET status='refunded' WHERE payment_id=%s", (payment_id,))
        self.conn.commit()
        print(f"💸 Payment {payment_id} refunded successfully!")

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
