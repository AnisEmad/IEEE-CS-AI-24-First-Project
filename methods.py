students = list()

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

    student_id = int(input("Enter ID of student to delete: "))
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
