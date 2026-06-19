
import streamlit as st

# Initialize session state
if "students" not in st.session_state:
    st.session_state.students = []

# Function to calculate average
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

# Function to assign grade
def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# App Title
st.title("🎓 Student Grade Calculator & Report Card")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Student", "View Students", "Class Report"]
)

# Add Student
if menu == "Add Student":
    st.header("Add Student")

    name = st.text_input("Student Name")
    score_input = st.text_input(
        "Enter scores separated by commas (Example: 85,90,78)"
    )

    if st.button("Add Student"):
        if name and score_input:
            try:
                scores = [float(score.strip()) for score in score_input.split(",")]

                valid = all(0 <= score <= 100 for score in scores)

                if valid:
                    avg = calculate_average(scores)
                    grade = get_letter_grade(avg)

                    student = {
                        "name": name,
                        "scores": scores,
                        "average": avg,
                        "grade": grade
                    }

                    st.session_state.students.append(student)

                    st.success(
                        f"Added {name} - Average: {avg:.2f} - Grade: {grade}"
                    )
                else:
                    st.error("Scores must be between 0 and 100.")
            except:
                st.error("Please enter valid numeric scores.")

# View Students
elif menu == "View Students":
    st.header("All Students")

    if st.session_state.students:
        for student in st.session_state.students:
            st.write(
                f"**{student['name']}** | "
                f"Scores: {student['scores']} | "
                f"Average: {student['average']:.2f} | "
                f"Grade: {student['grade']}"
            )
    else:
        st.info("No students added yet.")

# Class Report
elif menu == "Class Report":
    st.header("Class Report")

    students = st.session_state.students

    if students:
        highest = max(students, key=lambda x: x["average"])
        lowest = min(students, key=lambda x: x["average"])

        class_average = (
            sum(student["average"] for student in students)
            / len(students)
        )

        st.write(f"**Total Students:** {len(students)}")
        st.write(
            f"**Highest Average:** {highest['name']} "
            f"({highest['average']:.2f})"
        )
        st.write(
            f"**Lowest Average:** {lowest['name']} "
            f"({lowest['average']:.2f})"
        )
        st.write(f"**Class Average:** {class_average:.2f}")
    else:
        st.info("No student data available.")