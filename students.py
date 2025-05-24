from faker import Faker
import random
import sqlite3

class StudentDataGenerator:
    def __init__(self, db_name="placement_app.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.fake = Faker()
        random.seed(0)
        Faker.seed(0)

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            email TEXT,
            phone TEXT,
            enrollment_year INTEGER,
            course_batch TEXT,
            city TEXT,
            graduation_year INTEGER
        )
        ''')
        self.conn.commit()

    def insert_fake_students(self, num_students=100):
        genders = ['Male', 'Female', 'Other']
        batches = ['Batch A', 'Batch B', 'Batch C']

        for _ in range(num_students):
            name = self.fake.name()
            age = random.randint(18, 25)
            gender = random.choice(genders)
            email = self.fake.email()
            phone = self.fake.phone_number()
            enrollment_year = random.randint(2019, 2023)
            course_batch = random.choice(batches)
            city = self.fake.city()
            graduation_year = enrollment_year + 3

            self.cursor.execute('''
            INSERT INTO students (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year))
        
        self.conn.commit()

    def close(self):
        self.conn.close()

# Usage
if __name__ == "__main__":
    generator = StudentDataGenerator()
    generator.create_table()
    generator.insert_fake_students(num_students=100)
    generator.close()
