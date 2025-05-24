import sqlite3

class DatabaseManager:
    def __init__(self, db_name="placement_app.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=()):
        """Execute INSERT, UPDATE, DELETE"""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database Error: {e}")

    def fetch_all(self, query, params=()):
        """Execute SELECT query and return all results"""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Fetch Error: {e}")
            return []

    def fetch_one(self, query, params=()):
        """Execute SELECT query and return a single result"""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Fetch Error: {e}")
            return None

    def close(self):
        self.conn.close()
