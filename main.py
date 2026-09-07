import studentmanagement as sm

while True:
    print("\n Welcome to the Student Management App")
    print("1- View Student Details")
    print("2- Add Student Details")
    print("3- Update Student Details")
    print("4- Delete Student Details")
    print("5- Exit")

    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        sm.view_student()
    elif choice == 2:
        sm.add_student()
    elif choice == 3:
        sm.update_student()
    elif choice == 4:
        sm.delete_student()
    elif choice == 5:
        print("Thank you for using this application")
        break
    else:
        print("Please enter a valid choice")