import streamlit as st
import pandas as pd
from Student_Management_System import StudentManager

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = "Add Student"

st.sidebar.title("📚 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Add Student",
        "View Students",
        "Search Student",
        "Update Student",
        "Delete Student(s)"
    ],
    index=[
        "Add Student",
        "View Students",
        "Search Student",
        "Update Student",
        "Delete Student(s)"
    ].index(st.session_state.page)
)

st.session_state.page = page

st.markdown(
    """
    <style>
    .stDataFrame td {
        text-align: center !important;
    }
    .stDataFrame th {
        text-align: center !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎓 Student Management System")
st.write("Streamlit setup is successful 🚀")

if "manager" not in st.session_state:
    st.session_state.manager = StudentManager()

if "add_form_key" not in st.session_state:
    st.session_state.add_form_key = 0

if "add_name" not in st.session_state:
    st.session_state.add_name = ""

if "add_age" not in st.session_state:
    st.session_state.add_age = 1

if "add_course" not in st.session_state:
    st.session_state.add_course = ""

if "add_success" not in st.session_state:
    st.session_state.add_success = False

if "confirm_delete" not in st.session_state:
    st.session_state.confirm_delete = False

def show_success(msg):
    st.success(f"✅ {msg}")

def show_warning(msg):
    st.warning(f"⚠️ {msg}")

def show_error(msg):
    st.error(f"❌ {msg}")

def show_info(msg):
    st.info(f"ℹ️ {msg}")



if page == "Add Student":
    st.header("➕ Add Student")

    with st.form(key=f"add_student_form_{st.session_state.add_form_key}"):
        name = st.text_input("Name", placeholder="Enter full name")
        age = st.number_input("Age", min_value=1, value=1, step=1)
        course = st.text_input("Course", placeholder="e.g. CS, AI, ML")

        submitted = st.form_submit_button("Add Student")

    if submitted:
        if not name.strip():
            show_warning("Please enter student name.")
        elif not course.strip():
            show_warning("Please enter course name.")
        else:
            st.session_state.manager.add_student(name, age, course)
            show_success("Student added successfully.")

            # 🔑 FORCE FORM RESET
            st.session_state.add_form_key += 1

if page == "View Students":
    st.subheader("📋 View Students")
    
    students = st.session_state.manager.students
    
    if not students:
        show_info("No students have been added yet. Use the 'Add Student' section to get started.")
    else:
        df = pd.DataFrame(students)
        st.dataframe(df,use_container_width=True,hide_index=True)

if page == "Search Student":
    st.subheader("🔍 Search Student by ID")
    
    search_id = st.number_input("Enter Student ID",min_value=0,step=1,value=st.session_state.get("search_id",0),key="search_id")
    
    if st.button("Search"):
        if search_id == 0:
            show_warning("Please enter a valid student ID.")
        else:
            result = None
            for student in st.session_state.manager.students:
                if student["id"] == search_id:
                    result = student
                    break
            if result:
                show_success("Student found.")
                st.write(result)
            else:
                show_error("Student not found")

                st.session_state.search_id = 0

if page == "Delete Student(s)":
    st.subheader("🗑️ Delete Student(s)")
    ids_input = st.text_input("Enter Student ID(s)", placeholder="Example: 3 or 2,4,9", key="delete_ids")

    if st.button("Delete"):
        if not ids_input.strip():
            show_warning("Please enter atleast one student ID.")
        else:
            try:
                ids = [
                    int(i.strip())
                    for i in ids_input.split(",")
                    if i.strip().isdigit()
                ]

                if not ids:
                    show_warning("No valid student IDs found.")
                else:
                    students = st.session_state.manager.students
                    deleted_ids=[]

                    for sid in ids:
                        for student in students:
                            if student["id"]== sid:
                                students.remove(student)
                                deleted_ids.append(sid)
                                break
                    
                    if deleted_ids:
                        show_success(f"Delted student(s) with ID(s): {', '.join(map(str, deleted_ids))}")
                    else:
                        show_error("No matching students found.")
            except Exception:
                show_error("Invalid input format.")

                st.session_state.delete_ids = ""


if page == "Update Student":
    st.subheader("✏️ Update Student Details")
    
    update_id = st.number_input("Student ID",min_value=0,step=1,value=st.session_state.get("update_id", 0),key="update_id")
    
    students = st.session_state.manager.students
    student = next((s for s in students if s["id"] == update_id), None)
    
    if student:
        new_name= st.text_input("Name",value=student["name"])
        new_age= st.number_input("Age",min_value=1,step=1,value=student["age"])
        new_course=st.text_input("Course",value=student["course"])
        
        if st.button("Update Student"):
            student["name"] = new_name
            student["age"]=new_age
            student["course"]=new_course
            show_success("Successfully updated.")
            
    elif update_id != 0:
        show_warning("Student not found!")
        st.session_state.update_id = 0