import error_handling
students = list()
id = 0
def addStudent():
    """ method used for adding a student to a temproray list of dicts """
    global id
    id += 1
    print("Enter the details of the student: ")
    name = error_handling.handleString(input("Full name: "))
    age = error_handling.handleSignal(input("Age: "))
    grade = error_handling.handleSignal(input("Grade: "))
    email = error_handling.handleEmail(input("Email: "))
    address = error_handling.handleString(input("Address: "))
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


def searchStudent():
    """ method search for a student by name or id in the temp database"""
    global students
    student_id = 0
    if not students:
        print("There are no students to search for.")
        return

    try:
        search_by = input("Would you like to Search for a student by Name or ID: ")
        if search_by.lower() not in ['name', 'id']:
            print("Invalid input! ")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the student ID.")
        return

    search_value = input(f"Enter {search_by}: ")
    found = False

    for student in students:
        if  student['ID'] == int(search_value) or student['Name'] == search_value:
            print(f"The student was found Successfully ")
            print("\t\t\" The Student Info\"" )
            print("\t\t==================")
            for key, value in student.items():
                print(f"{key}: {value}")
                found = True
            break

    if not found:
        print(f" SORRY! Student was NOT found")


def updateStudentDetails():
    """ update student details method by ID , it can update all student details or One student detail """
    global students

    if not students:
        print("There are no students to update.")
        return

    try:
        student_id = int(input("Enter ID of student to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the student ID.")
        return

    for index, student in enumerate(students):
        if student['ID'] == student_id:
            print(f"The student who has this ID number: {student_id} was found Successfully ")
            update_type = int(input("Enter your command (choose number 1 or 2 ) : "
                                    "\n\t 1. Update All Student Details"
                                    "\n\t 2. Update One Value Of Student Details \n"))
            if update_type == 1:
                name = error_handling.handleString(input("Full name: "))
                age = error_handling.handleSignal(input("Age: "))
                grade = error_handling.handleSignal(input("Grade: "))
                email = error_handling.handleEmail(input("Email: "))
                address = error_handling.handleString(input("Address: "))

                students[index]['Name'] = name
                students[index]['Age'] = age
                students[index]['Grade'] = grade
                students[index]['Email'] = email
                students[index]['Address'] = address

                print("\n\t\"The New Student Details Has Successfully Updated To\"")

            elif update_type == 2:
                update_by_value = int(input("Enter your command (choose number of update value you want to update): "
                                            "\n\t 1.Name"
                                            "\n\t 2.Age"
                                            "\n\t 3.Grade"
                                            "\n\t 4.Email"
                                            "\n\t 5.Address\n"))

                if update_by_value == 1:
                    name = error_handling.handleString(input("Full name: "))
                    student['Name'] = name
                elif update_by_value == 2:
                    age = error_handling.handleSignal(input("Age: "))
                    student['Age'] = age
                elif update_by_value == 3:
                    grade = error_handling.handleSignal(input("Grade: "))
                    student['Grade'] = grade
                elif update_by_value == 4:
                    email = error_handling.handleEmail(input("Email: "))
                    student['Email'] = email
                elif update_by_value == 5:
                    address = error_handling.handleString(input("Address: "))
                    student['Address'] = address
                else:
                    print("Invalid command, Please Enter Number from 1 to 5.")
                update_value ={
                    1: 'Name',
                    2: 'Age',
                    3: 'Grade',
                    4: 'Email',
                    5: 'Address'
                }
                print(f"\t\"The {update_value[update_by_value]} Has Updated Successfully To\"")


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

        