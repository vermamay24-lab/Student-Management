students = []

def view_student():
    if(len(students) == 0):
        print("students Data not found")
    else:
        id = input("Enter student id: ")
        for student in students:
            if student["id"] == id:
                print(student)
            return
        print(f"Student Id {id} not found.")

def add_student():
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    student_class = input("Enter student class: ")

    students.append({"id": id, "name": name, "age": age, "student_class": student_class})

    print(f"Student Id {id} added successfully!")

def update_student():
    id = input("Enter student id: ")

    for student in students:
        if student["id"] == id:
            print("\nIf you want old value then simply press Enter")
            name = input(f"Enter student name: ({student['name']})" or student["name"])
            age = input(f"Enter student age: ({student['age']})" or student["age"])
            student_class = input(f"Enter student class: ({student['student_class']})" or student["student_class"])

            student["name"] = name
            student["age"] = age
            student["student_class"] = student_class

        print(f"Student Id {id} updated successfully!")
        return
    print(f"student id {id} not found.")

def delete_student():
    id = input("Enter student id: ")

    for student in students:
        if student["id"] == id:
            students.remove(student)
            print(f"Student Id {id} deleted successfully!")
            return
    print(f"student id {id} not found.")