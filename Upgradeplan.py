class UpgradePlan:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def upgrade_plan(self, user_id, new_plan):
        self.cursor.execute(
            "UPDATE users SET plan=%s WHERE user_id=%s",
            (new_plan, user_id)
        )
        self.conn.commit()
        print(f"🚀 User {user_id} upgraded to '{new_plan}' plan successfully!")

    def view_plan(self, user_id):
        self.cursor.execute("SELECT plan FROM users WHERE user_id=%s", (user_id,))
        plan = self.cursor.fetchone()
        if plan:
            print(f"📄 Current plan for User {user_id}: {plan[0]}")
        else:
            print("⚠️ User not found")

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
