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



def searchStudent():
    
    student_id=0
    
    if not students:
        print("There are no students to search for.")

    try:
        search_by = input("Would you like to Search for a student by Name or ID: ")
        if search_by.lower() == 'name':
            student_name = input("Enter Name of student to search for: ")
        elif search_by.lower() == 'id':
            student_id = int(input("Enter ID of student to search for: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the student ID.")
        return


    found = False

    for student in students:
        if student['ID'] == student_id or student['Name'] == student_name:
            print(f"The student was found Successfully ")
            for key, value in student.items():
                print(f"{key}: {value}")
                found = True
            break

    if not found:
        print(f" SORRY! Student was NOT found")


def updateStudentDetails():

    if not students:
        print("There are no students to update.")
        return

    try:
        student_id = int(input("Enter ID of student to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the student ID.")
        return

    updated = False

    for index, student in enumerate(students):
        if student['ID'] == student_id:
            print(f"The student who has this ID number: {student_id} was found Successfully ")
            update_type = int(input("Enter your command (choose number 1 or 2 ) : "
                                    "\n\t 1. Update All Student Details"
                                    "\n\t 2. Update One Value Of Student Details "))
            if update_type == 1:
                name = error_handling.handleString(input("Full name: "))
                age = error_handling.handleSignal(input("Age: "))
                grade = error_handling.handleSignal(input("Grade: "))
                email = error_handling.handleEmail(input("Email: "))
                address = error_handling.handleString(input("Address: "))
                student = {
                    "Name": name,
                    "Age": age,
                    "Grade": grade,
                    "Email": email,
                    "Address": address
                }
                students.insert(index, student)
            elif update_type == 2:
                update_by_value = input("Enter your command (choose number of update value you want to update): "
                                        "\n\t 1.Name"
                                        "\n\t 2.Age"
                                        "\n\t 3.Grade"
                                        "\n\t 4.Email"
                                        "\n\t 5.Address")

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
                    print("Invalid command, Enter numbers 1 to 5.")



def loadFromFile():
    file_list=''   # to store content of file 
    with open("database.txt","r") as file:
        file_list=f"[{file.read()}]"
        if file_list=='[]':
            print("file is empty :(")
        else:
            file_list=eval(file_list) # to convert str to tuple or list
            
            for i in file_list:   # to rem a dublicated value in list
                if i not in students:
                    students.append(i)
                else:
                    continue  
        print(file.closed)
        

def saveToFile():
    
    with open("database.txt","a") as file:
        with open("database.txt","r") as filee_test:
            test=filee_test.read()
        for i in range(0,len(students)):
            if test != '':
                   file.write(f", \n{str(students[i])}")
            else:
                file.write(f"{str(students[i])}")
            

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
