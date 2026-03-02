# 🎓 Student Management System (Streamlit App)

A clean and interactive **Student Management System** built using **Python** and **Streamlit**, supporting full CRUD operations with persistent storage.

---
# 🎓 Student Management System

🚀 Live App: https://sandeep-student-app.streamlit.app  

---

## Overview

## 🚀 Features
- Add new students
- View all students in a table
- Search student by ID
- Update student details
- Delete single or multiple students
- Persistent data storage using JSON
- Clean and user-friendly Streamlit UI

---

## 🛠 Tech Stack
- Python
- Streamlit
- Pandas
- JSON (for data persistence)

---

## 📂 Project Structure
Student-Management-System/
│
├── app.py # Streamlit frontend (UI logic)
├── Student_Management_System.py # Core backend logic (OOP + CRUD)
├── README.md # Project documentation
├── .gitignore # Files ignored by Git
└── students.json # Local data storage (auto-generated)
---
### 🔎 File Descriptions

- **app.py** → Handles Streamlit UI, navigation, and user interaction.
- **Student_Management_System.py** → Contains Student and StudentManager classes with CRUD logic.
- **students.json** → Stores student data persistently in JSON format.
- **.gitignore** → Prevents unnecessary files like venv and cache from being pushed to GitHub.

## 🏗 Architecture Overview

The project follows a clean separation of concerns:

- **Frontend Layer (Streamlit)** → Handles UI rendering and session management.
- **Business Logic Layer (OOP)** → Manages student operations using object-oriented design.
- **Persistence Layer (JSON File)** → Ensures data remains stored across sessions.

## ▶️ How to Run the Project

```bash
# Create virtual environment
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Install dependencies
pip install streamlit pandas

# Run app
streamlit run app.py
