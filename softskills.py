import sqlite3
import random

class SoftSkillsDataGenerator:
    def __init__(self, db_name="placement_app.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS soft_skills (
            soft_skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            communication INTEGER,
            teamwork INTEGER,
            presentation INTEGER,
            leadership INTEGER,
            critical_thinking INTEGER,
            interpersonal_skills INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
        ''')
        self.conn.commit()

    def insert_fake_soft_skills_data(self):
        self.cursor.execute("SELECT student_id FROM students")
        student_ids = [row[0] for row in self.cursor.fetchall()]

        for student_id in student_ids:
            communication = random.randint(50, 100)
            teamwork = random.randint(50, 100)
            presentation = random.randint(50, 100)
            leadership = random.randint(50, 100)
            critical_thinking = random.randint(50, 100)
            interpersonal_skills = random.randint(50, 100)

            self.cursor.execute('''
            INSERT INTO soft_skills (
                student_id, communication, teamwork, presentation,
                leadership, critical_thinking, interpersonal_skills
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills))

        self.conn.commit()

    def close(self):
        self.conn.close()

# Usage
if __name__ == "__main__":
    generator = SoftSkillsDataGenerator()
    generator.create_table()
    generator.insert_fake_soft_skills_data()
    generator.close()
