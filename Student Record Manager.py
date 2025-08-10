#Welcome to the Student Record Manager
print("Welcome to the Student Record Manager!")
# This program allows users to manage student records, including adding students, grades, checking enrollment, calculating averages, and listing students by course.
student_records = {}
# This function adds a new student to the records
def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {
            'Age': age,
            "grades" : set(),
            'Courses': set(courses)
        }
        print(f"Student '{name}' added successfully.")
# This function adds a grade for a student
def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]['grades'].add(grade)
        print(f"Grade '{grade}' added for student '{name}'.")
# This function checks if a student is enrolled in a specific course
def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    else:
        if course in student_records[name]['Courses']:
            print(f"Student '{name}' is enrolled in '{course}'.")
            return True
        else:
            print(f"Student '{name}' is not enrolled in '{course}'.")
            return False
# This function calculates the average grade for a student
def calculate_average(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    else:
        grade = student_records[name]['grades']
        if not grade:
            print(f"No grades found for student '{name}'.")
            return 0
        else:
            average = sum(grade) / len(grade)
            print(f"Average grade for student '{name}': {average:.2f}")
            return average
# This function lists all students enrolled in a specific course
def list_students_by_course(course):
    enrolled_students = []
    for name, details in student_records.items():
        if course in details['Courses']:
            enrolled_students.append(name)
    return enrolled_students
#This function filters students Top students based on the cutoff value or the limit value
def filter_top_students(limit_vaue):
    top_students = []
    for name, details in student_records.items():
        if calculate_average(name) >= limit_vaue:
            top_students.append(name)
    return top_students
# Example usage of the functions
add_student("Rachel", 100, ["Math", "Physics", "Chemistry"])
add_student("Vandana", 22, ["Math", "Biology"])
add_student("Jay", 23, ["Chemistry", "Physics"])
add_grade("Rachel", 90)
add_grade("Vandana", 85)
add_grade("Jay", 75)
add_grade("Rachel", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]