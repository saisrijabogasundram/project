class updateProfile:
    def __init__(self,cursor,conn):
        self.cursor = cursor
        self.conn = conn
    def update_profile(self, user_id, name, email, password):
        self.cursor.execute("UPDATE users SET name=%s, email=%s, password=%s WHERE user_id=%s",
                       (name, email, password, user_id))
        self.conn.commit()
        print(f"Profile {user_id} updated successfully!")
    def view_profile(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
        user = self.cursor.fetchone()
        if user:
            print(user)
        else:
            print("User not found")
    def close(self):
        self.cursor.close()
        self.conn.close()