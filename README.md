# Student-Management
Python Student Management System – A simple menu-driven application to manage student records using Python. Supports adding, viewing, updating, and deleting student details through CRUD operations.
# 🎓 Student Management System

A simple **Student Management System built with Python** that allows users to manage student records through a menu-driven command-line interface.

The application provides basic **CRUD (Create, Read, Update, Delete)** functionality for student information.

## 📌 Features

* ➕ Add Student Details
* 👀 View Student Details
* ✏️ Update Student Details
* 🗑️ Delete Student Details
* 🚪 Exit the application
* 🔍 Search students using Student ID
* ✅ Displays success/error messages for operations

## 🛠️ Technologies Used

* **Python 3**
* Python Lists
* Python Dictionaries
* Functions
* Loops
* Conditional Statements
* Modules

## 📂 Project Structure

```text
Student-Management-System/
│
├── main.py
├── studentmanagement.py
└── README.md
```

### `main.py`

Contains the main menu and controls the flow of the application.

The menu provides options to:

1. View Student Details
2. Add Student Details
3. Update Student Details
4. Delete Student Details
5. Exit

### `studentmanagement.py`

Contains the functions used to manage student records:

* `view_student()`
* `add_student()`
* `update_student()`
* `delete_student()`

Student information is stored in a Python list as dictionaries.

Each student record contains:

```python
{
    "id": id,
    "name": name,
    "age": age,
    "student_class": student_class
}
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Student-Management-System.git
```

### 2. Navigate to the project directory

```bash
cd Student-Management-System
```

### 3. Run the application

```bash
python main.py
```

## 💻 Application Menu

When the application starts, you will see:

```text
Welcome to the Student Management App

1- View Student Details
2- Add Student Details
3- Update Student Details
4- Delete Student Details
5- Exit
```

Enter the number corresponding to the operation you want to perform.

## 🔄 CRUD Operations

### Create

The **Add Student Details** option allows you to enter:

* Student ID
* Student Name
* Student Age
* Student Class

### Read

The **View Student Details** option allows you to search for a student using their Student ID.

### Update

The **Update Student Details** option allows you to modify existing student information.

### Delete

The **Delete Student Details** option removes a student record using their Student ID.

## 📚 Concepts Practiced

This project demonstrates practical usage of:

* Variables
* Lists
* Dictionaries
* Functions
* `if-elif-else`
* `for` loops
* `while` loops
* User input
* Modules and imports
* Basic CRUD operations

## 🎯 Learning Objective

The main purpose of this project is to practice **Python fundamentals and modular programming** by building a small real-world application.

It is suitable as a beginner Python project for understanding how different Python concepts can be combined to create a functional command-line application.

## 🔮 Future Improvements

The project can be extended by adding:

* 💾 File/database storage
* 🔐 User authentication
* 📊 Student marks and grades
* 🔎 Advanced search
* 📋 Display all students in a formatted table
* 🛡️ Input validation
* 🗄️ MySQL/PostgreSQL database integration
* 🌐 Web interface using Flask, FastAPI, or Django

## 👨‍💻 Author

**Mayank Verma**

---

⭐ If you found this project useful, consider giving the repository a star!
