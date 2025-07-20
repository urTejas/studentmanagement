import streamlit as st
from student_manager import Student, StudentManager

st.set_page_config(page_title="Student Manager", page_icon="🎓", layout="centered")
st.title("🎓 Student Management System")

# Initialize session state only once
if 'manager' not in st.session_state:
    st.session_state.manager = StudentManager()

manager = st.session_state.manager

# Sidebar
menu = st.sidebar.radio("Menu", ["Add Student", "View All Students", "Search Student"])


# Add student
if menu == "Add Student":
    st.header("Add New Student")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    course = st.selectbox("Course", ["BSC CS", "BSC IT", "MCA", "MSC CS", "Others"])

    if st.button("Add Student"):
        if name and course:
            new_student = Student(name, age, course)
            manager.add_student(new_student)
            st.success(f"Student {name} added successfully!")
        else:
            st.warning("Please fill all fields.")

# View students
elif menu == "View All Students":
    st.header("All Students")
    students = manager.get_all_students()
    if students:
        st.table(students)
    else:
        st.info("No students added yet.")

# Search student
elif menu == "Search Student":
    st.header("Search Student by Name")
    search_name = st.text_input("Enter student name to search")
    if st.button("Search"):
        results = manager.search_student(search_name)
        if results:
            st.table(results)
        else:
            st.warning("No student found.")
