import json
import os

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.students = json.load(f)
        else:
            self.students = []

    def save_students(self):
        with open(self.filename, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, name, age, course):
        new_id = max([s["id"] for s in self.students], default=0) + 1
        self.students.append({
            "id": new_id,
            "name": name,
            "age": age,
            "course": course
        })
        self.save_students()

    def update_student(self, student_id, name, age, course):
        for student in self.students:
            if student["id"] == student_id:
                student["name"] = name
                student["age"] = age
                student["course"] = course
                self.save_students()
                return True
            return False
        
    def delete_students_by_ids(self, ids):
        self.students = [s for s in self.students if s["id"] not in ids]
        self.save_students()