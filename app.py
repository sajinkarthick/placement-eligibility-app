import streamlit as st
from dbmanager import DatabaseManager
import pandas as pd
import altair as alt

# Initialize DB manager
db = DatabaseManager()

st.set_page_config(page_title="Placement Eligibility", layout="wide")
st.title("🎓 Placement Eligibility Filter")

# --- Sidebar filters ---
st.sidebar.header("🧪 Set Eligibility Criteria")

min_problems_solved = st.sidebar.slider("Minimum Problems Solved", 0, 200, 50)
min_soft_skills_score = st.sidebar.slider("Minimum Soft Skills Average Score", 0, 100, 75)
min_mock_score = st.sidebar.slider("Minimum Mock Interview Score", 0, 100, 60)

st.sidebar.markdown("—")

st.sidebar.caption("Note: Candidates must meet **all** thresholds above.")

# --- Query construction ---
query = """
SELECT 
    s.name, s.email, s.phone, s.course_batch, s.graduation_year, s.city,
    p.problems_solved, ss.communication, ss.teamwork, ss.presentation,
    ss.leadership, ss.critical_thinking, ss.interpersonal_skills,
    pl.mock_interview_score, pl.placement_status
FROM students s
JOIN programming p ON s.student_id = p.student_id
JOIN soft_skills ss ON s.student_id = ss.student_id
JOIN placements pl ON s.student_id = pl.student_id
"""

students = db.fetch_all(query)

# --- Filter logic ---
eligible_students = []

for row in students:
    (
        name, email, phone, batch, grad_year, city,
        problems_solved,
        comm, team, pres, leader, crit, interp,
        mock_score, status
    ) = row

    soft_avg = sum([comm, team, pres, leader, crit, interp]) / 6

    if (
        problems_solved >= min_problems_solved and
        soft_avg >= min_soft_skills_score and
        mock_score >= min_mock_score
    ):
        eligible_students.append({
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Batch": batch,
            "Graduation Year": grad_year,
            "City": city,
            "Problems Solved": problems_solved,
            "Soft Skills Avg": round(soft_avg, 2),
            "Mock Interview Score": mock_score,
            "Status": status
        })

# --- Display Results ---
st.subheader("✅ Eligible Students")

if eligible_students:
    st.dataframe(eligible_students, use_container_width=True)
    st.success(f"Found {len(eligible_students)} eligible students.")
else:
    st.warning("No students match the criteria.")

# Close DB
db.close()

