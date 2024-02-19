students = list()
id = 0
def addStudent():
    """ method used for adding a student to a temproray list of dicts """
    global id
    id += 1
    print("Enter the details of the student: ")
    name = input("Full name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    email = input("Email: ")
    address = input("Address: ")
    student = {
        "Name": name,
        "Age": age,
        "Grade": grade,
        "ID": id,
        "Email": email,
        "Address": address
        }
    students.append(student)
    print("student added sucessfully")


def viewStudent():
    """ method prints all the students in the temp database """
    for student in students:
        print("=============================================================")
        for key, value in student.items():
            print(f"{key}: {value}")
    print("=============================================================")
    
    
def deleteStudentById():
    """
    Delete a student from the list of students by ID.

    This function prompts the user to input the ID of the student they want to delete
    It then iterates over the list of students, searching for a student with a matching ID
    If found the student is removed from the list
    If not found a message indicating that the student was not found is printed

    Parameters:
    None

    Returns:
    None
    """

    global students

    if not students:
        print("There are no students to delete.")
        return

    try:
        student_id = int(input("Enter ID of student to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the student ID.")
        return

    found = False

    for student in students:
        if student['ID'] == student_id:
            students.remove(student)
            found = True
            break

    if found:
        print("Student deleted successfully")
    else:
        print("Student not found")

        