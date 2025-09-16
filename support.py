class Support:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def submit_ticket(self, ticket_id, user_id, subject, description, status='open'):
        self.cursor.execute(
            "INSERT INTO support_tickets (ticket_id, user_id, subject, description, status) VALUES (%s, %s, %s, %s, %s)",
            (ticket_id, user_id, subject, description, status)
        )
        self.conn.commit()
        print(f"🎫 Support ticket {ticket_id} submitted successfully!")

    def view_tickets(self, user_id):
        self.cursor.execute("SELECT * FROM support_tickets WHERE user_id=%s", (user_id,))
        tickets = self.cursor.fetchall()
        if tickets:
            for row in tickets:
                print(row)
        else:
            print("⚠️ No tickets found for this user.")

    def update_ticket_status(self, ticket_id, status):
        self.cursor.execute("UPDATE support_tickets SET status=%s WHERE ticket_id=%s",
                            (status, ticket_id))
        self.conn.commit()
        print(f"✅ Support ticket {ticket_id} updated to '{status}' successfully!")

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
  