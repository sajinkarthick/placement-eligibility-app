import sqlite3
import random

class ProgrammingDataGenerator:
    def __init__(self, db_name="placement_app.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS programming (
            programming_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            language TEXT,
            problems_solved INTEGER,
            assessments_completed INTEGER,
            mini_projects INTEGER,
            certifications_earned INTEGER,
            latest_project_score INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        ''')
        self.conn.commit()

    def insert_fake_programming_data(self):
        languages = ['Python', 'SQL', 'JavaScript']
        
        # Get all student IDs
        self.cursor.execute("SELECT student_id FROM students")
        student_ids = [row[0] for row in self.cursor.fetchall()]

        for student_id in student_ids:
            language = random.choice(languages)
            problems_solved = random.randint(10, 200)
            assessments_completed = random.randint(0, 10)
            mini_projects = random.randint(0, 5)
            certifications_earned = random.randint(0, 3)
            latest_project_score = random.randint(40, 100)

            self.cursor.execute('''
            INSERT INTO programming (student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score))

        self.conn.commit()

    def close(self):
        self.conn.close()

# Usage
if __name__ == "__main__":
    generator = ProgrammingDataGenerator()
    generator.create_table()
    generator.insert_fake_programming_data()
    generator.close()
