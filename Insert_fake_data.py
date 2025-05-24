import sqlite3
from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_students(n=100):
    students = []
    current_year = datetime.now().year
    batches = ['Batch A', 'Batch B', 'Batch C']
    genders = ['Male', 'Female', 'Other']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

    for _ in range(n):
        name = fake.name()
        age = random.randint(18, 25)
        gender = random.choice(genders)
        email = fake.email()
        phone = fake.phone_number()
        enrollment_year = random.randint(current_year - 4, current_year)
        course_batch = random.choice(batches)
        city = random.choice(cities)
        graduation_year = enrollment_year + 4
        students.append((name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year))
    return students

def generate_programming(student_ids):
    languages = ['Python', 'SQL', 'Java', 'C++']
    programming = []

    for student_id in student_ids:
        language = random.choice(languages)
        problems_solved = random.randint(0, 200)
        assessments_completed = random.randint(0, 10)
        mini_projects = random.randint(0, 5)
        certifications_earned = random.randint(0, 3)
        latest_project_score = round(random.uniform(50, 100), 2)
        programming.append((student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score))
    return programming

def generate_soft_skills(student_ids):
    soft_skills = []
    for student_id in student_ids:
        communication = random.randint(50, 100)
        teamwork = random.randint(50, 100)
        presentation = random.randint(50, 100)
        leadership = random.randint(50, 100)
        critical_thinking = random.randint(50, 100)
        interpersonal_skills = random.randint(50, 100)
        soft_skills.append((student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills))
    return soft_skills

def generate_placements(student_ids):
    statuses = ['Ready', 'Not Ready', 'Placed']
    companies = ['Google', 'Microsoft', 'Amazon', 'Facebook', 'None']
    placements = []

    for student_id in student_ids:
        mock_interview_score = random.randint(30, 100)
        internships_completed = random.randint(0, 3)
        placement_status = random.choices(statuses, weights=[0.3, 0.4, 0.3])[0]
        company_name = random.choice(companies) if placement_status == 'Placed' else None
        placement_package = round(random.uniform(30000, 120000), 2) if placement_status == 'Placed' else None
        interview_rounds_cleared = random.randint(0, 5) if placement_status == 'Placed' else 0
        placement_date = fake.date_between(start_date='-2y', end_date='today').isoformat() if placement_status == 'Placed' else None
        placements.append((student_id, mock_interview_score, internships_completed, placement_status, company_name, placement_package, interview_rounds_cleared, placement_date))
    return placements

def insert_data():
    conn = sqlite3.connect('placement_app.db')
    cursor = conn.cursor()

    # Generate students
    students = generate_students(100)
    cursor.executemany("""
        INSERT INTO students (name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, students)
    conn.commit()

    # Fetch student_ids
    cursor.execute("SELECT student_id FROM students")
    student_ids = [row[0] for row in cursor.fetchall()]

    # Generate and insert programming data
    programming = generate_programming(student_ids)
    cursor.executemany("""
        INSERT INTO programming (student_id, language, problems_solved, assessments_completed, mini_projects, certifications_earned, latest_project_score)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, programming)
    conn.commit()

    # Generate and insert soft skills data
    soft_skills = generate_soft_skills(student_ids)
    cursor.executemany("""
        INSERT INTO soft_skills (student_id, communication, teamwork, presentation, leadership, critical_thinking, interpersonal_skills)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, soft_skills)
    conn.commit()

    # Generate and insert placements data
    placements = generate_placements(student_ids)
    cursor.executemany("""
        INSERT INTO placements (student_id, mock_interview_score, internships_completed, placement_status, company_name, placement_package, interview_rounds_cleared, placement_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, placements)
    conn.commit()

    conn.close()
    print("Fake data inserted successfully!")

if __name__ == "__main__":
    insert_data()
