import sqlite3

def create_tables(db_name="placement_app.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Students Table
    cursor.execute("""
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
    """)

    # Programming Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS programming (
        programming_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        language TEXT,
        problems_solved INTEGER,
        assessments_completed INTEGER,
        mini_projects INTEGER,
        certifications_earned INTEGER,
        latest_project_score REAL,
        FOREIGN KEY(student_id) REFERENCES students(student_id)
    )
    """)

    # Soft Skills Table
    cursor.execute("""
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
    """)

    # Placements Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS placements (
        placement_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        mock_interview_score INTEGER,
        internships_completed INTEGER,
        placement_status TEXT,
        company_name TEXT,
        placement_package REAL,
        interview_rounds_cleared INTEGER,
        placement_date TEXT,
        FOREIGN KEY(student_id) REFERENCES students(student_id)
    )
    """)

    conn.commit()
    conn.close()
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()
