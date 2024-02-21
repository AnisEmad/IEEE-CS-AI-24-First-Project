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

    #global students

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


def searchStudent():
    print("")


def updateStudentDetails():
    print("")


def loadFromFile():
    file_list=''   # to store content of file 
    with open("database.txt","r") as file:
        file_list=file.read()
        file_list=eval(file_list) # to convert str to tuple or list
        
    for i in file_list:   # to rem a dublicated value in list
        if i not in students:
            students.append(i)
        else:
            continue

        print(file.closed)


def saveToFile():
    print(students)
    with open("database.txt","w") as file:
        file.write(str(students))


def showToRead():
    num_of_student=0
    with open("database.txt","w") as file:
        
        for student in students:
            file.write(f"\n===========================Student {num_of_student}================================== \n\n")
            
            for key, value in student.items():
                file.write(f"{key}:  {value} \n")
                          
            num_of_student+=1
    ending = input("press to enter if u ending read from file : ")
    with open("database.txt", "w") as file:
        file.truncate(0)  # Truncate the file to remove all data to add avaluable data
    saveToFile()




#    ┌───────────┐ │ └ ┘  

