def get_student_data():
    roll_no =int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    
    m1 = float(input("Enter marks for Subject 1: "))
    m2 = float(input("Enter marks for Subject 2: "))
    m3 = float(input("Enter marks for Subject 3: "))
    
    average = (m1 + m2 + m3) / 3
    grade = calculate_grade(average)
    
    return {
        "roll_no": roll_no,
        "name": name,
        "average": round(average, 2),
        "grade": grade
    }

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

def display_records(students_list):
    print(f"{'Roll No':<10} {'Name':<15} {'Average':<10} {'Grade':<5}")
    print("-" * 45)
    
    for student in students_list:
        print(f"{student['roll_no']:<10} {student['name']:<15} {student['average']:<10} {student['grade']:<5}")

def main():
    students = []
    
    for i in range(1, 4):
        print(f"\n--- Enter Details for Student {i} ---")
        student_record = get_student_data()
        students.append(student_record)
    
    display_records(students)

if __name__ == "__main__":
    main()
